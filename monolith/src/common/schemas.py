from datetime import datetime
from typing import Any, Dict, Generic, List, Optional, TypeVar
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field
from pydantic.generics import GenericModel

T = TypeVar("T")


class BaseSchema(BaseModel):
    """Base schema with common fields."""

    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class PaginatedResponse(GenericModel, Generic[T]):
    """Generic paginated response schema."""

    items: List[T]
    total: int
    page: int
    size: int
    pages: int


class ErrorResponse(BaseModel):
    """Error response schema."""

    detail: str
    code: Optional[str] = None
    errors: Optional[List[Dict[str, Any]]] = None


class UserBase(BaseSchema):
    """Base user schema."""

    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: bool = True
    is_verified: bool = False


class UserCreate(BaseModel):
    """User creation schema."""

    email: EmailStr
    password: str = Field(..., min_length=8)
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserUpdate(BaseModel):
    """User update schema."""

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: Optional[bool] = None


class UserProfileBase(BaseSchema):
    """Base user profile schema."""

    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    job_title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    website: Optional[str] = None


class UserProfileCreate(BaseModel):
    """User profile creation schema."""

    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    job_title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    website: Optional[str] = None


class UserProfileUpdate(BaseModel):
    """User profile update schema."""

    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    job_title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    website: Optional[str] = None


class Token(BaseModel):
    """Token schema."""

    access_token: str
    token_type: str = "bearer"
    expires_in: int
    refresh_token: Optional[str] = None


class TokenPayload(BaseModel):
    """Token payload schema."""

    sub: UUID
    exp: int
    iat: int
    type: str


class PasswordResetRequest(BaseModel):
    """Password reset request schema."""

    email: EmailStr


class PasswordReset(BaseModel):
    """Password reset schema."""

    token: str
    password: str = Field(..., min_length=8)


class EmailVerificationRequest(BaseModel):
    """Email verification request schema."""

    email: EmailStr


class EmailVerification(BaseModel):
    """Email verification schema."""

    token: str


class SearchQuery(BaseModel):
    """Search query schema."""

    query: str
    page: int = 1
    size: int = 10
    filters: Optional[Dict[str, Any]] = None
    sort: Optional[str] = None


class SearchResponse(BaseModel):
    """Search response schema."""

    items: List[Dict[str, Any]]
    total: int
    page: int
    size: int
    pages: int
    aggregations: Optional[Dict[str, Any]] = None


class Event(BaseModel):
    """Event schema."""

    event_type: str
    event_id: str
    timestamp: datetime
    data: Dict[str, Any] 