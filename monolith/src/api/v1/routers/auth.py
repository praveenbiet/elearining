"""
Authentication API router
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.common.database import get_db
from src.modules.auth.services.authentication_service import AuthenticationService
from src.modules.auth.schemas.internal import (
    UserCreate,
    LoginResponse,
    TokenResponse,
    TokenRefreshRequest
)

router = APIRouter(prefix="/auth")

@router.post("/register", response_model=LoginResponse, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Register a new user
    """
    auth_service = AuthenticationService(db)
    try:
        user, token = auth_service.register_user(user_data)
        return {
            "user": user,
            "token": token
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/login", response_model=LoginResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Login with username and password
    """
    auth_service = AuthenticationService(db)
    try:
        user, token = auth_service.authenticate_user(
            email=form_data.username,
            password=form_data.password
        )
        return {
            "user": user,
            "token": token
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(
    refresh_data: TokenRefreshRequest,
    db: Session = Depends(get_db)
):
    """
    Refresh access token using refresh token
    """
    auth_service = AuthenticationService(db)
    try:
        token = auth_service.refresh_token(refresh_data.refresh_token)
        return token
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.post("/logout")
async def logout(
    refresh_data: TokenRefreshRequest,
    db: Session = Depends(get_db)
):
    """
    Logout user by invalidating their refresh token
    """
    auth_service = AuthenticationService(db)
    auth_service.invalidate_token(refresh_data.refresh_token)
    return {"detail": "Successfully logged out"} 