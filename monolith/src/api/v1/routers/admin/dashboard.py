"""
Admin Dashboard API router
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.common.database import get_db
from src.modules.auth.services.authentication_service import get_current_user
from src.modules.identity.schemas.internal import UserResponse
from src.modules.admin.services.admin_dashboard_service import AdminDashboardService
from src.modules.admin.schemas.admin import DashboardStatsResponse

router = APIRouter()

@router.get("", response_model=DashboardStatsResponse)
async def get_dashboard_stats(
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    """
    Get dashboard statistics for admin users
    """
    # Check if user is an admin
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions to access admin dashboard"
        )
    
    dashboard_service = AdminDashboardService(db)
    stats = dashboard_service.get_dashboard_stats()
    return stats

@router.get("/recent-activity")
async def get_recent_activity(
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    """
    Get recent user activity for admin dashboard
    """
    # Check if user is an admin
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions to access admin dashboard"
        )
    
    dashboard_service = AdminDashboardService(db)
    activity = dashboard_service.get_recent_activity(limit)
    return activity

@router.get("/revenue-stats")
async def get_revenue_stats(
    period: str = "month", # day, week, month, year
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    """
    Get revenue statistics for admin dashboard
    """
    # Check if user is an admin
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions to access admin dashboard"
        )
    
    dashboard_service = AdminDashboardService(db)
    revenue_stats = dashboard_service.get_revenue_stats(period)
    return revenue_stats 