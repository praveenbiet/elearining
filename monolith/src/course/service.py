from typing import List, Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from ..common.exceptions import NotFoundException, UnauthorizedException
from ..common.schemas import CourseCreate, CourseUpdate, ModuleCreate, ModuleUpdate, LessonCreate, LessonUpdate
from .model import Course, Module, Lesson
from .repository import CourseRepository, ModuleRepository, LessonRepository


class CourseService:
    def __init__(self, session: AsyncSession):
        self.course_repo = CourseRepository(session)
        self.module_repo = ModuleRepository(session)
        self.lesson_repo = LessonRepository(session)

    async def create_course(self, instructor_id: UUID, course_data: CourseCreate) -> Course:
        course = Course(
            title=course_data.title,
            description=course_data.description,
            instructor_id=instructor_id,
            level=course_data.level,
            duration=course_data.duration,
            price=course_data.price,
        )
        return await self.course_repo.create(course)

    async def get_course(self, course_id: UUID) -> Course:
        course = await self.course_repo.get_by_id(course_id)
        if not course:
            raise NotFoundException("Course not found")
        return course

    async def get_instructor_courses(self, instructor_id: UUID) -> List[Course]:
        return await self.course_repo.get_by_instructor(instructor_id)

    async def update_course(self, course_id: UUID, instructor_id: UUID, course_data: CourseUpdate) -> Course:
        course = await self.get_course(course_id)
        if course.instructor_id != instructor_id:
            raise UnauthorizedException("Not authorized to update this course")

        if course_data.title:
            course.title = course_data.title
        if course_data.description:
            course.description = course_data.description
        if course_data.level:
            course.level = course_data.level
        if course_data.duration:
            course.duration = course_data.duration
        if course_data.price:
            course.price = course_data.price
        if course_data.is_published is not None:
            course.is_published = course_data.is_published

        return await self.course_repo.update(course)

    async def delete_course(self, course_id: UUID, instructor_id: UUID) -> None:
        course = await self.get_course(course_id)
        if course.instructor_id != instructor_id:
            raise UnauthorizedException("Not authorized to delete this course")
        await self.course_repo.delete(course)

    async def create_module(self, course_id: UUID, instructor_id: UUID, module_data: ModuleCreate) -> Module:
        course = await self.get_course(course_id)
        if course.instructor_id != instructor_id:
            raise UnauthorizedException("Not authorized to add modules to this course")

        module = Module(
            course_id=course_id,
            title=module_data.title,
            description=module_data.description,
            order=module_data.order,
        )
        return await self.module_repo.create(module)

    async def get_module(self, module_id: UUID) -> Module:
        module = await self.module_repo.get_by_id(module_id)
        if not module:
            raise NotFoundException("Module not found")
        return module

    async def get_course_modules(self, course_id: UUID) -> List[Module]:
        return await self.module_repo.get_by_course(course_id)

    async def update_module(self, module_id: UUID, instructor_id: UUID, module_data: ModuleUpdate) -> Module:
        module = await self.get_module(module_id)
        course = await self.get_course(module.course_id)
        if course.instructor_id != instructor_id:
            raise UnauthorizedException("Not authorized to update this module")

        if module_data.title:
            module.title = module_data.title
        if module_data.description:
            module.description = module_data.description
        if module_data.order:
            module.order = module_data.order

        return await self.module_repo.update(module)

    async def delete_module(self, module_id: UUID, instructor_id: UUID) -> None:
        module = await self.get_module(module_id)
        course = await self.get_course(module.course_id)
        if course.instructor_id != instructor_id:
            raise UnauthorizedException("Not authorized to delete this module")
        await self.module_repo.delete(module)

    async def create_lesson(self, module_id: UUID, instructor_id: UUID, lesson_data: LessonCreate) -> Lesson:
        module = await self.get_module(module_id)
        course = await self.get_course(module.course_id)
        if course.instructor_id != instructor_id:
            raise UnauthorizedException("Not authorized to add lessons to this module")

        lesson = Lesson(
            module_id=module_id,
            title=lesson_data.title,
            description=lesson_data.description,
            content=lesson_data.content,
            order=lesson_data.order,
            duration=lesson_data.duration,
        )
        return await self.lesson_repo.create(lesson)

    async def get_lesson(self, lesson_id: UUID) -> Lesson:
        lesson = await self.lesson_repo.get_by_id(lesson_id)
        if not lesson:
            raise NotFoundException("Lesson not found")
        return lesson

    async def get_module_lessons(self, module_id: UUID) -> List[Lesson]:
        return await self.lesson_repo.get_by_module(module_id)

    async def update_lesson(self, lesson_id: UUID, instructor_id: UUID, lesson_data: LessonUpdate) -> Lesson:
        lesson = await self.get_lesson(lesson_id)
        module = await self.get_module(lesson.module_id)
        course = await self.get_course(module.course_id)
        if course.instructor_id != instructor_id:
            raise UnauthorizedException("Not authorized to update this lesson")

        if lesson_data.title:
            lesson.title = lesson_data.title
        if lesson_data.description:
            lesson.description = lesson_data.description
        if lesson_data.content:
            lesson.content = lesson_data.content
        if lesson_data.order:
            lesson.order = lesson_data.order
        if lesson_data.duration:
            lesson.duration = lesson_data.duration

        return await self.lesson_repo.update(lesson)

    async def delete_lesson(self, lesson_id: UUID, instructor_id: UUID) -> None:
        lesson = await self.get_lesson(lesson_id)
        module = await self.get_module(lesson.module_id)
        course = await self.get_course(module.course_id)
        if course.instructor_id != instructor_id:
            raise UnauthorizedException("Not authorized to delete this lesson")
        await self.lesson_repo.delete(lesson) 