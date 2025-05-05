from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..common.kafka import produce_event


@dataclass
class UserCreatedEvent:
    user_id: UUID
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    timestamp: datetime = datetime.utcnow()

    async def publish(self):
        await produce_event(
            "user.created",
            {
                "user_id": str(self.user_id),
                "email": self.email,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "timestamp": self.timestamp.isoformat(),
            },
        )


@dataclass
class UserUpdatedEvent:
    user_id: UUID
    first_name: Optional[str]
    last_name: Optional[str]
    is_active: Optional[bool]
    timestamp: datetime = datetime.utcnow()

    async def publish(self):
        await produce_event(
            "user.updated",
            {
                "user_id": str(self.user_id),
                "first_name": self.first_name,
                "last_name": self.last_name,
                "is_active": self.is_active,
                "timestamp": self.timestamp.isoformat(),
            },
        )


@dataclass
class UserDeletedEvent:
    user_id: UUID
    timestamp: datetime = datetime.utcnow()

    async def publish(self):
        await produce_event(
            "user.deleted",
            {
                "user_id": str(self.user_id),
                "timestamp": self.timestamp.isoformat(),
            },
        )


@dataclass
class UserProfileCreatedEvent:
    user_id: UUID
    bio: Optional[str]
    avatar_url: Optional[str]
    job_title: Optional[str]
    company: Optional[str]
    location: Optional[str]
    website: Optional[str]
    timestamp: datetime = datetime.utcnow()

    async def publish(self):
        await produce_event(
            "user.profile.created",
            {
                "user_id": str(self.user_id),
                "bio": self.bio,
                "avatar_url": self.avatar_url,
                "job_title": self.job_title,
                "company": self.company,
                "location": self.location,
                "website": self.website,
                "timestamp": self.timestamp.isoformat(),
            },
        )


@dataclass
class UserProfileUpdatedEvent:
    user_id: UUID
    bio: Optional[str]
    avatar_url: Optional[str]
    job_title: Optional[str]
    company: Optional[str]
    location: Optional[str]
    website: Optional[str]
    timestamp: datetime = datetime.utcnow()

    async def publish(self):
        await produce_event(
            "user.profile.updated",
            {
                "user_id": str(self.user_id),
                "bio": self.bio,
                "avatar_url": self.avatar_url,
                "job_title": self.job_title,
                "company": self.company,
                "location": self.location,
                "website": self.website,
                "timestamp": self.timestamp.isoformat(),
            },
        ) 