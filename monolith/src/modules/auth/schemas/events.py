"""
Event schema definitions for the Auth module
"""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class UserCreatedEvent(BaseModel):
    """
    Event emitted when a new user is created
    """
    user_id: str = Field(..., description="ID of the created user")
    email: str = Field(..., description="Email of the created user")
    role: str = Field(..., description="Role of the created user")
    created_at: datetime = Field(..., description="Timestamp when the user was created")

class UserUpdatedEvent(BaseModel):
    """
    Event emitted when a user is updated
    """
    user_id: str = Field(..., description="ID of the updated user")
    email: Optional[str] = Field(None, description="Updated email, if changed")
    role: Optional[str] = Field(None, description="Updated role, if changed")
    is_active: Optional[bool] = Field(None, description="Updated active status, if changed")
    updated_at: datetime = Field(..., description="Timestamp when the user was updated")

class UserLoginEvent(BaseModel):
    """
    Event emitted when a user logs in
    """
    user_id: str = Field(..., description="ID of the user who logged in")
    email: str = Field(..., description="Email of the user who logged in")
    login_at: datetime = Field(..., description="Timestamp of the login")
    ip_address: Optional[str] = Field(None, description="IP address from which the login occurred")
    user_agent: Optional[str] = Field(None, description="User agent from which the login occurred")

class UserLogoutEvent(BaseModel):
    """
    Event emitted when a user logs out
    """
    user_id: str = Field(..., description="ID of the user who logged out")
    logout_at: datetime = Field(..., description="Timestamp of the logout")

class PasswordChangedEvent(BaseModel):
    """
    Event emitted when a user changes their password
    """
    user_id: str = Field(..., description="ID of the user who changed their password")
    changed_at: datetime = Field(..., description="Timestamp of the password change")
    was_reset: bool = Field(False, description="Whether this was a password reset operation") 