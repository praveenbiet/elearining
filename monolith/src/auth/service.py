from typing import Optional
from uuid import UUID

from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from ..common.exceptions import NotFoundException, UnauthorizedException
from ..common.schemas import UserCreate, UserUpdate, UserProfileCreate, UserProfileUpdate
from .model import User, UserProfile
from .repository import UserRepository, UserProfileRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    def __init__(self, session: AsyncSession):
        self.user_repo = UserRepository(session)
        self.profile_repo = UserProfileRepository(session)

    async def create_user(self, user_data: UserCreate) -> User:
        # Check if user already exists
        existing_user = await self.user_repo.get_by_email(user_data.email)
        if existing_user:
            raise UnauthorizedException("Email already registered")

        # Create new user
        user = User(
            email=user_data.email,
            password_hash=pwd_context.hash(user_data.password),
            first_name=user_data.first_name,
            last_name=user_data.last_name,
        )
        return await self.user_repo.create(user)

    async def get_user(self, user_id: UUID) -> Optional[User]:
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise NotFoundException("User not found")
        return user

    async def update_user(self, user_id: UUID, user_data: UserUpdate) -> User:
        user = await self.get_user(user_id)
        if user_data.first_name:
            user.first_name = user_data.first_name
        if user_data.last_name:
            user.last_name = user_data.last_name
        if user_data.is_active is not None:
            user.is_active = user_data.is_active
        return await self.user_repo.update(user)

    async def delete_user(self, user_id: UUID) -> None:
        user = await self.get_user(user_id)
        await self.user_repo.delete(user)

    async def verify_password(self, email: str, password: str) -> Optional[User]:
        user = await self.user_repo.get_by_email(email)
        if not user or not pwd_context.verify(password, user.password_hash):
            return None
        return user

    async def create_profile(self, user_id: UUID, profile_data: UserProfileCreate) -> UserProfile:
        user = await self.get_user(user_id)
        profile = UserProfile(
            user_id=user.id,
            bio=profile_data.bio,
            avatar_url=profile_data.avatar_url,
            job_title=profile_data.job_title,
            company=profile_data.company,
            location=profile_data.location,
            website=profile_data.website,
        )
        return await self.profile_repo.create(profile)

    async def get_profile(self, user_id: UUID) -> Optional[UserProfile]:
        profile = await self.profile_repo.get_by_user_id(user_id)
        if not profile:
            raise NotFoundException("Profile not found")
        return profile

    async def update_profile(self, user_id: UUID, profile_data: UserProfileUpdate) -> UserProfile:
        profile = await self.get_profile(user_id)
        if profile_data.bio:
            profile.bio = profile_data.bio
        if profile_data.avatar_url:
            profile.avatar_url = profile_data.avatar_url
        if profile_data.job_title:
            profile.job_title = profile_data.job_title
        if profile_data.company:
            profile.company = profile_data.company
        if profile_data.location:
            profile.location = profile_data.location
        if profile_data.website:
            profile.website = profile_data.website
        return await self.profile_repo.update(profile) 