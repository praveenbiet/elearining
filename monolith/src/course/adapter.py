from typing import List, Optional
from uuid import UUID

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..common.database import get_session
from ..common.schemas import CourseBase, ModuleBase, LessonBase
from .model import Course, Module, Lesson
from .service import CourseService


async def get_course_service(session: AsyncSession = Depends(get_session)) -> CourseService:
    return CourseService(session)


def to_course_schema(course: Course) -> CourseBase:
    return CourseBase(
        id=course.id,
        title=course.title,
        description=course.description,
        instructor_id=course.instructor_id,
        level=course.level,
        duration=course.duration,
        price=course.price,
        is_published=course.is_published,
        created_at=course.created_at,
        updated_at=course.updated_at,
    )


def to_module_schema(module: Module) -> ModuleBase:
    return ModuleBase(
        id=module.id,
        course_id=module.course_id,
        title=module.title,
        description=module.description,
        order=module.order,
        created_at=module.created_at,
        updated_at=module.updated_at,
    )


def to_lesson_schema(lesson: Lesson) -> LessonBase:
    return LessonBase(
        id=lesson.id,
        module_id=lesson.module_id,
        title=lesson.title,
        description=lesson.description,
        content=lesson.content,
        order=lesson.order,
        duration=lesson.duration,
        created_at=lesson.created_at,
        updated_at=lesson.updated_at,
    ) 