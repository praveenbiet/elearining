"""
Admin API router
"""
from fastapi import APIRouter

from src.api.v1.routers.admin import (
    dashboard,
    users,
    courses,
    settings
)

router = APIRouter()

# Include admin-specific routers
router.include_router(dashboard.router, prefix="/dashboard", tags=["Admin Dashboard"])
router.include_router(users.router, prefix="/users", tags=["Admin Users"])
router.include_router(courses.router, prefix="/courses", tags=["Admin Courses"])
router.include_router(settings.router, prefix="/settings", tags=["Admin Settings"]) 