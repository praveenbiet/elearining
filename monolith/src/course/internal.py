from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status

from ..common.schemas import (
    CourseBase,
    CourseCreate,
    CourseUpdate,
    ModuleBase,
    ModuleCreate,
    ModuleUpdate,
    LessonBase,
    LessonCreate,
    LessonUpdate,
)
from .adapter import (
    get_course_service,
    to_course_schema,
    to_module_schema,
    to_lesson_schema,
)
from .events import (
    CourseCreatedEvent,
    CourseUpdatedEvent,
    CourseDeletedEvent,
    ModuleCreatedEvent,
    ModuleUpdatedEvent,
    ModuleDeletedEvent,
    LessonCreatedEvent,
    LessonUpdatedEvent,
    LessonDeletedEvent,
)
from .service import CourseService

router = APIRouter(prefix="/courses", tags=["courses"])


@router.post("", response_model=CourseBase, status_code=status.HTTP_201_CREATED)
async def create_course(
    course_data: CourseCreate,
    instructor_id: UUID,
    course_service: CourseService = Depends(get_course_service),
):
    course = await course_service.create_course(instructor_id, course_data)
    event = CourseCreatedEvent(
        course_id=course.id,
        instructor_id=course.instructor_id,
        title=course.title,
        description=course.description,
        level=course.level,
        duration=course.duration,
        price=course.price,
    )
    await event.publish()
    return to_course_schema(course)


@router.get("/{course_id}", response_model=CourseBase)
async def get_course(
    course_id: UUID,
    course_service: CourseService = Depends(get_course_service),
):
    course = await course_service.get_course(course_id)
    return to_course_schema(course)


@router.get("/instructor/{instructor_id}", response_model=List[CourseBase])
async def get_instructor_courses(
    instructor_id: UUID,
    course_service: CourseService = Depends(get_course_service),
):
    courses = await course_service.get_instructor_courses(instructor_id)
    return [to_course_schema(course) for course in courses]


@router.put("/{course_id}", response_model=CourseBase)
async def update_course(
    course_id: UUID,
    course_data: CourseUpdate,
    instructor_id: UUID,
    course_service: CourseService = Depends(get_course_service),
):
    course = await course_service.update_course(course_id, instructor_id, course_data)
    event = CourseUpdatedEvent(
        course_id=course.id,
        instructor_id=course.instructor_id,
        title=course.title,
        description=course.description,
        level=course.level,
        duration=course.duration,
        price=course.price,
        is_published=course.is_published,
    )
    await event.publish()
    return to_course_schema(course)


@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(
    course_id: UUID,
    instructor_id: UUID,
    course_service: CourseService = Depends(get_course_service),
):
    await course_service.delete_course(course_id, instructor_id)
    event = CourseDeletedEvent(course_id=course_id, instructor_id=instructor_id)
    await event.publish()


@router.post("/{course_id}/modules", response_model=ModuleBase, status_code=status.HTTP_201_CREATED)
async def create_module(
    course_id: UUID,
    module_data: ModuleCreate,
    instructor_id: UUID,
    course_service: CourseService = Depends(get_course_service),
):
    module = await course_service.create_module(course_id, instructor_id, module_data)
    event = ModuleCreatedEvent(
        module_id=module.id,
        course_id=module.course_id,
        title=module.title,
        description=module.description,
        order=module.order,
    )
    await event.publish()
    return to_module_schema(module)


@router.get("/{course_id}/modules", response_model=List[ModuleBase])
async def get_course_modules(
    course_id: UUID,
    course_service: CourseService = Depends(get_course_service),
):
    modules = await course_service.get_course_modules(course_id)
    return [to_module_schema(module) for module in modules]


@router.put("/modules/{module_id}", response_model=ModuleBase)
async def update_module(
    module_id: UUID,
    module_data: ModuleUpdate,
    instructor_id: UUID,
    course_service: CourseService = Depends(get_course_service),
):
    module = await course_service.update_module(module_id, instructor_id, module_data)
    event = ModuleUpdatedEvent(
        module_id=module.id,
        course_id=module.course_id,
        title=module.title,
        description=module.description,
        order=module.order,
    )
    await event.publish()
    return to_module_schema(module)


@router.delete("/modules/{module_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_module(
    module_id: UUID,
    instructor_id: UUID,
    course_service: CourseService = Depends(get_course_service),
):
    module = await course_service.get_module(module_id)
    await course_service.delete_module(module_id, instructor_id)
    event = ModuleDeletedEvent(module_id=module_id, course_id=module.course_id)
    await event.publish()


@router.post("/modules/{module_id}/lessons", response_model=LessonBase, status_code=status.HTTP_201_CREATED)
async def create_lesson(
    module_id: UUID,
    lesson_data: LessonCreate,
    instructor_id: UUID,
    course_service: CourseService = Depends(get_course_service),
):
    lesson = await course_service.create_lesson(module_id, instructor_id, lesson_data)
    event = LessonCreatedEvent(
        lesson_id=lesson.id,
        module_id=lesson.module_id,
        title=lesson.title,
        description=lesson.description,
        content=lesson.content,
        order=lesson.order,
        duration=lesson.duration,
    )
    await event.publish()
    return to_lesson_schema(lesson)


@router.get("/modules/{module_id}/lessons", response_model=List[LessonBase])
async def get_module_lessons(
    module_id: UUID,
    course_service: CourseService = Depends(get_course_service),
):
    lessons = await course_service.get_module_lessons(module_id)
    return [to_lesson_schema(lesson) for lesson in lessons]


@router.put("/lessons/{lesson_id}", response_model=LessonBase)
async def update_lesson(
    lesson_id: UUID,
    lesson_data: LessonUpdate,
    instructor_id: UUID,
    course_service: CourseService = Depends(get_course_service),
):
    lesson = await course_service.update_lesson(lesson_id, instructor_id, lesson_data)
    event = LessonUpdatedEvent(
        lesson_id=lesson.id,
        module_id=lesson.module_id,
        title=lesson.title,
        description=lesson.description,
        content=lesson.content,
        order=lesson.order,
        duration=lesson.duration,
    )
    await event.publish()
    return to_lesson_schema(lesson)


@router.delete("/lessons/{lesson_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lesson(
    lesson_id: UUID,
    instructor_id: UUID,
    course_service: CourseService = Depends(get_course_service),
):
    lesson = await course_service.get_lesson(lesson_id)
    await course_service.delete_lesson(lesson_id, instructor_id)
    event = LessonDeletedEvent(lesson_id=lesson_id, module_id=lesson.module_id)
    await event.publish() 