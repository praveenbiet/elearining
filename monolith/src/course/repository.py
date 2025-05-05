from typing import List, Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .model import Course, Module, Lesson


class CourseRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, course: Course) -> Course:
        self.session.add(course)
        await self.session.commit()
        await self.session.refresh(course)
        return course

    async def get_by_id(self, course_id: UUID) -> Optional[Course]:
        result = await self.session.execute(
            select(Course).where(Course.id == course_id)
        )
        return result.scalar_one_or_none()

    async def get_by_instructor(self, instructor_id: UUID) -> List[Course]:
        result = await self.session.execute(
            select(Course).where(Course.instructor_id == instructor_id)
        )
        return result.scalars().all()

    async def update(self, course: Course) -> Course:
        await self.session.commit()
        await self.session.refresh(course)
        return course

    async def delete(self, course: Course) -> None:
        await self.session.delete(course)
        await self.session.commit()


class ModuleRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, module: Module) -> Module:
        self.session.add(module)
        await self.session.commit()
        await self.session.refresh(module)
        return module

    async def get_by_id(self, module_id: UUID) -> Optional[Module]:
        result = await self.session.execute(
            select(Module).where(Module.id == module_id)
        )
        return result.scalar_one_or_none()

    async def get_by_course(self, course_id: UUID) -> List[Module]:
        result = await self.session.execute(
            select(Module)
            .where(Module.course_id == course_id)
            .order_by(Module.order)
        )
        return result.scalars().all()

    async def update(self, module: Module) -> Module:
        await self.session.commit()
        await self.session.refresh(module)
        return module

    async def delete(self, module: Module) -> None:
        await self.session.delete(module)
        await self.session.commit()


class LessonRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, lesson: Lesson) -> Lesson:
        self.session.add(lesson)
        await self.session.commit()
        await self.session.refresh(lesson)
        return lesson

    async def get_by_id(self, lesson_id: UUID) -> Optional[Lesson]:
        result = await self.session.execute(
            select(Lesson).where(Lesson.id == lesson_id)
        )
        return result.scalar_one_or_none()

    async def get_by_module(self, module_id: UUID) -> List[Lesson]:
        result = await self.session.execute(
            select(Lesson)
            .where(Lesson.module_id == module_id)
            .order_by(Lesson.order)
        )
        return result.scalars().all()

    async def update(self, lesson: Lesson) -> Lesson:
        await self.session.commit()
        await self.session.refresh(lesson)
        return lesson

    async def delete(self, lesson: Lesson) -> None:
        await self.session.delete(lesson)
        await self.session.commit() 