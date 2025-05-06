"""
Token value object in the authentication domain
"""
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
import uuid
import jwt

from src.common.config import settings

@dataclass
class Token:
    """
    Value object representing a JWT authentication token
    """
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

    @classmethod
    def create_for_user(cls, user_id: str, email: str, role: str) -> "Token":
        """
        Create access and refresh tokens for a user
        """
        # Create access token with shorter expiry
        access_token_expires = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token_payload = {
            "sub": user_id,
            "email": email,
            "role": role,
            "exp": access_token_expires,
            "iat": datetime.utcnow(),
            "jti": str(uuid.uuid4())
        }
        access_token = cls._create_jwt(access_token_payload)
        
        # Create refresh token with longer expiry
        refresh_token_expires = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        refresh_token_payload = {
            "sub": user_id,
            "exp": refresh_token_expires,
            "iat": datetime.utcnow(),
            "jti": str(uuid.uuid4()),
            "type": "refresh"
        }
        refresh_token = cls._create_jwt(refresh_token_payload)
        
        return cls(
            access_token=access_token,
            refresh_token=refresh_token
        )

    @staticmethod
    def _create_jwt(payload: Dict[str, Any]) -> str:
        """
        Create a JWT with the provided payload
        """
        return jwt.encode(
            payload=payload,
            key=settings.JWT_SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM
        )

    @staticmethod
    def decode_token(token: str) -> Dict[str, Any]:
        """
        Decode and validate a JWT token
        """
        try:
            payload = jwt.decode(
                token,
                key=settings.JWT_SECRET_KEY,
                algorithms=[settings.JWT_ALGORITHM]
            )
            return payload
        except jwt.PyJWTError as e:
            raise ValueError(f"Invalid token: {str(e)}")

    @classmethod
    def refresh(cls, refresh_token: str, user_id: str, email: str, role: str) -> "Token":
        """
        Create a new token pair using a valid refresh token
        """
        # Validate the refresh token
        try:
            payload = cls.decode_token(refresh_token)
            if payload.get("type") != "refresh" or payload.get("sub") != user_id:
                raise ValueError("Invalid refresh token")
        except ValueError:
            raise ValueError("Invalid or expired refresh token")
            
        # Create new token pair
        return cls.create_for_user(user_id, email, role) 