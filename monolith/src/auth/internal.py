from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..common.database import get_session
from ..common.schemas import (
    UserCreate,
    UserUpdate,
    UserProfileCreate,
    UserProfileUpdate,
    UserBase,
    UserProfileBase,
)
from .adapter import (
    get_auth_service,
    get_current_user,
    to_user_schema,
    to_user_profile_schema,
)
from .events import (
    UserCreatedEvent,
    UserUpdatedEvent,
    UserDeletedEvent,
    UserProfileCreatedEvent,
    UserProfileUpdatedEvent,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/users", response_model=UserBase, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate,
    auth_service: AuthService = Depends(get_auth_service),
):
    user = await auth_service.create_user(user_data)
    event = UserCreatedEvent(
        user_id=user.id,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
    )
    await event.publish()
    return to_user_schema(user)


@router.get("/users/me", response_model=UserBase)
async def get_me(user: User = Depends(get_current_user)):
    return to_user_schema(user)


@router.put("/users/me", response_model=UserBase)
async def update_me(
    user_data: UserUpdate,
    user: User = Depends(get_current_user),
    auth_service: AuthService = Depends(get_auth_service),
):
    updated_user = await auth_service.update_user(user.id, user_data)
    event = UserUpdatedEvent(
        user_id=updated_user.id,
        first_name=updated_user.first_name,
        last_name=updated_user.last_name,
        is_active=updated_user.is_active,
    )
    await event.publish()
    return to_user_schema(updated_user)


@router.delete("/users/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_me(
    user: User = Depends(get_current_user),
    auth_service: AuthService = Depends(get_auth_service),
):
    await auth_service.delete_user(user.id)
    event = UserDeletedEvent(user_id=user.id)
    await event.publish()


@router.post("/users/me/profile", response_model=UserProfileBase, status_code=status.HTTP_201_CREATED)
async def create_profile(
    profile_data: UserProfileCreate,
    user: User = Depends(get_current_user),
    auth_service: AuthService = Depends(get_auth_service),
):
    profile = await auth_service.create_profile(user.id, profile_data)
    event = UserProfileCreatedEvent(
        user_id=user.id,
        bio=profile.bio,
        avatar_url=profile.avatar_url,
        job_title=profile.job_title,
        company=profile.company,
        location=profile.location,
        website=profile.website,
    )
    await event.publish()
    return to_user_profile_schema(profile)


@router.get("/users/me/profile", response_model=UserProfileBase)
async def get_profile(
    user: User = Depends(get_current_user),
    auth_service: AuthService = Depends(get_auth_service),
):
    profile = await auth_service.get_profile(user.id)
    return to_user_profile_schema(profile)


@router.put("/users/me/profile", response_model=UserProfileBase)
async def update_profile(
    profile_data: UserProfileUpdate,
    user: User = Depends(get_current_user),
    auth_service: AuthService = Depends(get_auth_service),
):
    profile = await auth_service.update_profile(user.id, profile_data)
    event = UserProfileUpdatedEvent(
        user_id=user.id,
        bio=profile.bio,
        avatar_url=profile.avatar_url,
        job_title=profile.job_title,
        company=profile.company,
        location=profile.location,
        website=profile.website,
    )
    await event.publish()
    return to_user_profile_schema(profile) 