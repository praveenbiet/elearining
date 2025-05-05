from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..common.kafka import produce_event


@dataclass
class CourseCreatedEvent:
    course_id: UUID
    instructor_id: UUID
    title: str
    description: Optional[str]
    level: Optional[str]
    duration: Optional[int]
    price: Optional[int]
    timestamp: datetime = datetime.utcnow()

    async def publish(self):
        await produce_event(
            "course.created",
            {
                "course_id": str(self.course_id),
                "instructor_id": str(self.instructor_id),
                "title": self.title,
                "description": self.description,
                "level": self.level,
                "duration": self.duration,
                "price": self.price,
                "timestamp": self.timestamp.isoformat(),
            },
        )


@dataclass
class CourseUpdatedEvent:
    course_id: UUID
    instructor_id: UUID
    title: Optional[str]
    description: Optional[str]
    level: Optional[str]
    duration: Optional[int]
    price: Optional[int]
    is_published: Optional[bool]
    timestamp: datetime = datetime.utcnow()

    async def publish(self):
        await produce_event(
            "course.updated",
            {
                "course_id": str(self.course_id),
                "instructor_id": str(self.instructor_id),
                "title": self.title,
                "description": self.description,
                "level": self.level,
                "duration": self.duration,
                "price": self.price,
                "is_published": self.is_published,
                "timestamp": self.timestamp.isoformat(),
            },
        )


@dataclass
class CourseDeletedEvent:
    course_id: UUID
    instructor_id: UUID
    timestamp: datetime = datetime.utcnow()

    async def publish(self):
        await produce_event(
            "course.deleted",
            {
                "course_id": str(self.course_id),
                "instructor_id": str(self.instructor_id),
                "timestamp": self.timestamp.isoformat(),
            },
        )


@dataclass
class ModuleCreatedEvent:
    module_id: UUID
    course_id: UUID
    title: str
    description: Optional[str]
    order: int
    timestamp: datetime = datetime.utcnow()

    async def publish(self):
        await produce_event(
            "module.created",
            {
                "module_id": str(self.module_id),
                "course_id": str(self.course_id),
                "title": self.title,
                "description": self.description,
                "order": self.order,
                "timestamp": self.timestamp.isoformat(),
            },
        )


@dataclass
class ModuleUpdatedEvent:
    module_id: UUID
    course_id: UUID
    title: Optional[str]
    description: Optional[str]
    order: Optional[int]
    timestamp: datetime = datetime.utcnow()

    async def publish(self):
        await produce_event(
            "module.updated",
            {
                "module_id": str(self.module_id),
                "course_id": str(self.course_id),
                "title": self.title,
                "description": self.description,
                "order": self.order,
                "timestamp": self.timestamp.isoformat(),
            },
        )


@dataclass
class ModuleDeletedEvent:
    module_id: UUID
    course_id: UUID
    timestamp: datetime = datetime.utcnow()

    async def publish(self):
        await produce_event(
            "module.deleted",
            {
                "module_id": str(self.module_id),
                "course_id": str(self.course_id),
                "timestamp": self.timestamp.isoformat(),
            },
        )


@dataclass
class LessonCreatedEvent:
    lesson_id: UUID
    module_id: UUID
    title: str
    description: Optional[str]
    content: Optional[str]
    order: int
    duration: Optional[int]
    timestamp: datetime = datetime.utcnow()

    async def publish(self):
        await produce_event(
            "lesson.created",
            {
                "lesson_id": str(self.lesson_id),
                "module_id": str(self.module_id),
                "title": self.title,
                "description": self.description,
                "content": self.content,
                "order": self.order,
                "duration": self.duration,
                "timestamp": self.timestamp.isoformat(),
            },
        )


@dataclass
class LessonUpdatedEvent:
    lesson_id: UUID
    module_id: UUID
    title: Optional[str]
    description: Optional[str]
    content: Optional[str]
    order: Optional[int]
    duration: Optional[int]
    timestamp: datetime = datetime.utcnow()

    async def publish(self):
        await produce_event(
            "lesson.updated",
            {
                "lesson_id": str(self.lesson_id),
                "module_id": str(self.module_id),
                "title": self.title,
                "description": self.description,
                "content": self.content,
                "order": self.order,
                "duration": self.duration,
                "timestamp": self.timestamp.isoformat(),
            },
        )


@dataclass
class LessonDeletedEvent:
    lesson_id: UUID
    module_id: UUID
    timestamp: datetime = datetime.utcnow()

    async def publish(self):
        await produce_event(
            "lesson.deleted",
            {
                "lesson_id": str(self.lesson_id),
                "module_id": str(self.module_id),
                "timestamp": self.timestamp.isoformat(),
            },
        ) 