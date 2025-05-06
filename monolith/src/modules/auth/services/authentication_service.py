"""
Authentication service for user login and registration
"""
from typing import Tuple, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.common.database import get_db
from src.modules.auth.domain.user import User
from src.modules.auth.domain.password import Password
from src.modules.auth.domain.token import Token
from src.modules.auth.persistence.user_repository import UserRepository
from src.modules.auth.models.user import UserModel
from src.modules.auth.schemas.internal import UserResponse

# OAuth2 password bearer token scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

class AuthenticationService:
    """
    Service for handling user authentication, registration, and token management
    """
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)

    def register_user(self, user_data: dict) -> Tuple[UserResponse, str]:
        """
        Register a new user with email and password
        """
        # Check if email is already registered
        if self.user_repository.get_by_email(user_data["email"]):
            raise ValueError("Email already registered")

        # Create password value object and validate it
        try:
            password = Password.from_plain_text(user_data["password"])
        except ValueError as e:
            raise ValueError(str(e))

        # Create user domain entity
        user = User.create(
            email=user_data["email"],
            password=password,
            role=user_data.get("role", "student")
        )

        # Save user to database
        db_user = self.user_repository.create(user)
        
        # Generate token
        token = Token.create_for_user(
            user_id=db_user.id,
            email=db_user.email,
            role=db_user.role
        )

        # Return user data and token
        return UserResponse(
            id=db_user.id,
            email=db_user.email,
            name=user_data.get("name", ""),
            role=db_user.role,
            created_at=db_user.created_at,
            updated_at=db_user.updated_at
        ), token

    def authenticate_user(self, email: str, password: str) -> Tuple[UserResponse, str]:
        """
        Authenticate a user with email and password
        """
        # Get user from database
        db_user = self.user_repository.get_by_email(email)
        if not db_user:
            raise ValueError("Invalid credentials")

        # Check if user is active
        if not db_user.is_active:
            raise ValueError("User account is inactive")

        # Verify password
        password_obj = Password(value=password)
        if not password_obj.verify(db_user.password_hash):
            raise ValueError("Invalid credentials")

        # Record login
        db_user.record_login()
        self.user_repository.update(db_user)

        # Generate token
        token = Token.create_for_user(
            user_id=db_user.id,
            email=db_user.email,
            role=db_user.role
        )

        # Return user data and token
        return UserResponse(
            id=db_user.id,
            email=db_user.email,
            name=db_user.name if hasattr(db_user, "name") else "",
            role=db_user.role,
            created_at=db_user.created_at,
            updated_at=db_user.updated_at
        ), token

    def refresh_token(self, refresh_token: str) -> Token:
        """
        Generate a new token pair from a valid refresh token
        """
        try:
            # Decode and validate refresh token
            payload = Token.decode_token(refresh_token)
            
            # Check if it's a refresh token
            if payload.get("type") != "refresh":
                raise ValueError("Invalid token type")
            
            # Get user from database
            user_id = payload.get("sub")
            if not user_id:
                raise ValueError("Invalid token")
                
            db_user = self.user_repository.get_by_id(user_id)
            if not db_user or not db_user.is_active:
                raise ValueError("User not found or inactive")
            
            # Generate new token pair
            return Token.refresh(
                refresh_token,
                user_id=db_user.id,
                email=db_user.email,
                role=db_user.role
            )
        except ValueError as e:
            raise ValueError(f"Token refresh failed: {str(e)}")

    def invalidate_token(self, refresh_token: str) -> None:
        """
        Invalidate a refresh token (for logout)
        Note: In a production system, this would typically add the token to a blacklist
        or use a token revocation strategy involving Redis or another fast data store
        """
        # Here we would typically add the token to a blacklist
        # For the sake of simplicity, we're not implementing a full token blacklist system
        pass


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> UserResponse:
    """
    Get the current authenticated user from the access token
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decode and validate token
        payload = Token.decode_token(token)
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except ValueError:
        raise credentials_exception
    
    # Get user from database
    user_repository = UserRepository(db)
    user = user_repository.get_by_id(user_id)
    if user is None:
        raise credentials_exception
    
    # Return user data
    return UserResponse(
        id=user.id,
        email=user.email,
        name=user.name if hasattr(user, "name") else "",
        role=user.role,
        created_at=user.created_at,
        updated_at=user.updated_at
    ) 