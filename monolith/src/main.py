from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from .common.config import settings
from .common.logger import setup_logging
from .common.middlewares import RequestLoggingMiddleware
from .api.v1.routers import (
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
    admin,
)

# Setup logging
setup_logging()

# Create FastAPI app
app = FastAPI(
    title="E-Learning Platform API",
    description="API for the E-Learning Platform",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOSTS)
app.add_middleware(RequestLoggingMiddleware)

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(identity.router, prefix="/api/v1/identity", tags=["identity"])
app.include_router(courses.router, prefix="/api/v1/courses", tags=["courses"])
app.include_router(videos.router, prefix="/api/v1/videos", tags=["videos"])
app.include_router(assessments.router, prefix="/api/v1/assessments", tags=["assessments"])
app.include_router(learning_paths.router, prefix="/api/v1/learning-paths", tags=["learning-paths"])
app.include_router(user_progress.router, prefix="/api/v1/user-progress", tags=["user-progress"])
app.include_router(search.router, prefix="/api/v1/search", tags=["search"])
app.include_router(recommendations.router, prefix="/api/v1/recommendations", tags=["recommendations"])
app.include_router(discussions.router, prefix="/api/v1/discussions", tags=["discussions"])
app.include_router(subscriptions.router, prefix="/api/v1/subscriptions", tags=["subscriptions"])
app.include_router(billing.router, prefix="/api/v1/billing", tags=["billing"])
app.include_router(notifications.router, prefix="/api/v1/notifications", tags=["notifications"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["admin"])

@app.get("/")
async def root():
    return {"message": "Welcome to the E-Learning Platform API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 