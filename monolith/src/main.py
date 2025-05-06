"""
E-Learning Platform Monolith API
Main FastAPI application initialization and configuration
"""
import logging
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.common.config import settings
from src.common.logger import configure_logging
from src.common.database import get_db
from src.api.v1.routers import (
    auth,
    identity,
    courses,
    videos,
    assessments,
    learning_paths,
    user_progress,
    search,
    recommendations,
    discussions,
    subscriptions,
    billing,
    notifications,
    admin
)

# Configure logging
configure_logging()
logger = logging.getLogger(__name__)

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description="E-Learning Platform API",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
@app.get("/api/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}

# API v1 routers
app.include_router(auth.router, prefix="/api/v1", tags=["Authentication"])
app.include_router(identity.router, prefix="/api/v1", tags=["Identity"])
app.include_router(courses.router, prefix="/api/v1", tags=["Courses"])
app.include_router(videos.router, prefix="/api/v1", tags=["Videos"])
app.include_router(assessments.router, prefix="/api/v1", tags=["Assessments"])
app.include_router(learning_paths.router, prefix="/api/v1", tags=["Learning Paths"])
app.include_router(user_progress.router, prefix="/api/v1", tags=["User Progress"])
app.include_router(search.router, prefix="/api/v1", tags=["Search"])
app.include_router(recommendations.router, prefix="/api/v1", tags=["Recommendations"])
app.include_router(discussions.router, prefix="/api/v1", tags=["Discussions"])
app.include_router(subscriptions.router, prefix="/api/v1", tags=["Subscriptions"])
app.include_router(billing.router, prefix="/api/v1", tags=["Billing"])
app.include_router(notifications.router, prefix="/api/v1", tags=["Notifications"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["Admin"])

# Startup and shutdown events
@app.on_event("startup")
async def startup_event():
    logger.info("Starting up the application")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down the application")

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True) 