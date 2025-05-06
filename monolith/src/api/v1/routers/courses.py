"""
Courses API router
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from src.common.database import get_db
from src.modules.auth.services.authentication_service import get_current_user
from src.modules.course.services.course_management_service import CourseManagementService
from src.modules.course.schemas.internal import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    CourseListResponse,
    ModuleResponse,
    ModuleCreate,
    ModuleUpdate,
    LessonResponse,
    LessonCreate,
    LessonUpdate
)
from src.modules.identity.schemas.internal import UserResponse

router = APIRouter(prefix="/courses")

@router.get("", response_model=List[CourseListResponse])
async def list_courses(
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    category: Optional[str] = None,
    level: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Get a list of courses with optional filtering
    """
    course_service = CourseManagementService(db)
    courses = course_service.get_courses(
        skip=skip,
        limit=limit,
        search=search,
        category=category,
        level=level
    )
    return courses

@router.get("/{course_id}", response_model=CourseResponse)
async def get_course(
    course_id: str,
    db: Session = Depends(get_db)
):
    """
    Get a course by ID
    """
    course_service = CourseManagementService(db)
    course = course_service.get_course(course_id)
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    return course

@router.post("", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(
    course_data: CourseCreate,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    """
    Create a new course
    """
    # Check if user has instructor or admin role
    if current_user.role not in ["instructor", "admin"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions to create a course"
        )
    
    course_service = CourseManagementService(db)
    try:
        course = course_service.create_course(course_data, current_user.id)
        return course
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.put("/{course_id}", response_model=CourseResponse)
async def update_course(
    course_id: str,
    course_data: CourseUpdate,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    """
    Update a course
    """
    course_service = CourseManagementService(db)
    # Retrieve the course to check ownership
    course = course_service.get_course(course_id)
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    
    # Check if user owns the course or is an admin
    if course.instructor_id != current_user.id and current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions to update this course"
        )
    
    try:
        updated_course = course_service.update_course(course_id, course_data)
        return updated_course
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(
    course_id: str,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    """
    Delete a course
    """
    course_service = CourseManagementService(db)
    # Retrieve the course to check ownership
    course = course_service.get_course(course_id)
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    
    # Check if user owns the course or is an admin
    if course.instructor_id != current_user.id and current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions to delete this course"
        )
    
    course_service.delete_course(course_id)
    return None

# Module endpoints

@router.get("/{course_id}/modules", response_model=List[ModuleResponse])
async def list_modules(
    course_id: str,
    db: Session = Depends(get_db)
):
    """
    Get all modules for a course
    """
    course_service = CourseManagementService(db)
    # Check if course exists
    course = course_service.get_course(course_id)
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    
    modules = course_service.get_modules(course_id)
    return modules

@router.post("/{course_id}/modules", response_model=ModuleResponse, status_code=status.HTTP_201_CREATED)
async def create_module(
    course_id: str,
    module_data: ModuleCreate,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    """
    Create a new module for a course
    """
    course_service = CourseManagementService(db)
    # Check if course exists and user has permission
    course = course_service.get_course(course_id)
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    
    # Check if user owns the course or is an admin
    if course.instructor_id != current_user.id and current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions to modify this course"
        )
    
    try:
        module = course_service.create_module(course_id, module_data)
        return module
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

# Lesson endpoints (similar pattern)

@router.post("/{course_id}/modules/{module_id}/lessons", response_model=LessonResponse, status_code=status.HTTP_201_CREATED)
async def create_lesson(
    course_id: str,
    module_id: str,
    lesson_data: LessonCreate,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    """
    Create a new lesson within a module
    """
    course_service = CourseManagementService(db)
    # Check if course and module exist and user has permission
    course = course_service.get_course(course_id)
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    
    # Check module
    module = course_service.get_module(module_id)
    if not module or module.course_id != course_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Module not found or doesn't belong to the specified course"
        )
    
    # Check if user owns the course or is an admin
    if course.instructor_id != current_user.id and current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions to modify this course"
        )
    
    try:
        lesson = course_service.create_lesson(module_id, lesson_data)
        return lesson
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        ) 