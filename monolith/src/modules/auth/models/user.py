"""
SQLAlchemy model for User entities
"""
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.common.database import Base

class UserModel(Base):
    """
    SQLAlchemy model for users table
    """
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    last_login = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    profile = relationship("UserProfileModel", back_populates="user", uselist=False)
    courses = relationship("CourseModel", back_populates="instructor", foreign_keys="CourseModel.instructor_id")
    enrollments = relationship("EnrollmentModel", back_populates="user")
    assessment_attempts = relationship("AssessmentAttemptModel", back_populates="user")
    progress_records = relationship("UserProgressModel", back_populates="user")
    discussions = relationship("DiscussionPostModel", back_populates="author")
    subscriptions = relationship("SubscriptionModel", back_populates="user") 