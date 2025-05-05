from typing import Optional
from uuid import UUID

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..common.database import get_session
from ..common.oidc import get_oidc_user, require_oidc_auth
from ..common.schemas import UserBase, UserProfileBase
from .model import User, UserProfile
from .service import AuthService


async def get_auth_service(session: AsyncSession = Depends(get_session)) -> AuthService:
    return AuthService(session)


def to_user_schema(user: User) -> UserBase:
    return UserBase(
        id=user.id,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        is_active=user.is_active,
        is_verified=user.is_verified,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )


def to_user_profile_schema(profile: UserProfile) -> UserProfileBase:
    return UserProfileBase(
        id=profile.id,
        user_id=profile.user_id,
        bio=profile.bio,
        avatar_url=profile.avatar_url,
        job_title=profile.job_title,
        company=profile.company,
        location=profile.location,
        website=profile.website,
        created_at=profile.created_at,
        updated_at=profile.updated_at,
    )


async def get_current_user(
    user: dict = Depends(require_oidc_auth),
    auth_service: AuthService = Depends(get_auth_service),
) -> User:
    return await auth_service.get_user(UUID(user["sub"]))


async def get_current_user_optional(
    user: Optional[dict] = Depends(get_oidc_user),
    auth_service: AuthService = Depends(get_auth_service),
) -> Optional[User]:
    if not user:
        return None
    return await auth_service.get_user(UUID(user["sub"])) 