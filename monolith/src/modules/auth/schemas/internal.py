"""
Internal schema definitions for the Auth module
"""
from pydantic import BaseModel, Field, EmailStr, validator
from datetime import datetime
from typing import Optional, List

class UserCreate(BaseModel):
    """
    Schema for creating a new user
    """
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., min_length=8, description="User's password")
    name: Optional[str] = Field(None, description="User's full name")
    role: Optional[str] = Field("student", description="User's role (student, instructor, admin)")

    @validator("role")
    def validate_role(cls, v):
        allowed_roles = ["student", "instructor", "admin"]
        if v not in allowed_roles:
            raise ValueError(f"Role must be one of {allowed_roles}")
        return v

class UserUpdate(BaseModel):
    """
    Schema for updating a user
    """
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    role: Optional[str] = None

    @validator("role")
    def validate_role(cls, v):
        if v is not None:
            allowed_roles = ["student", "instructor", "admin"]
            if v not in allowed_roles:
                raise ValueError(f"Role must be one of {allowed_roles}")
        return v

    @validator("password")
    def validate_password(cls, v):
        if v is not None and len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return v

class UserResponse(BaseModel):
    """
    Schema for user data in responses
    """
    id: str
    email: str
    name: Optional[str] = None
    role: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class TokenResponse(BaseModel):
    """
    Schema for token data in responses
    """
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenRefreshRequest(BaseModel):
    """
    Schema for refreshing a token
    """
    refresh_token: str

class LoginResponse(BaseModel):
    """
    Schema for login response
    """
    user: UserResponse
    token: TokenResponse 