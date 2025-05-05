from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import relationship

from ..common.database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(PGUUID(as_uuid=True), primary_key=True, default=UUID)
    title = Column(String, nullable=False)
    description = Column(Text)
    instructor_id = Column(PGUUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    level = Column(String)  # beginner, intermediate, advanced
    duration = Column(Integer)  # in minutes
    price = Column(Integer)  # in cents
    is_published = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    instructor = relationship("User", back_populates="courses")
    modules = relationship("Module", back_populates="course", cascade="all, delete-orphan")


class Module(Base):
    __tablename__ = "modules"

    id = Column(PGUUID(as_uuid=True), primary_key=True, default=UUID)
    course_id = Column(PGUUID(as_uuid=True), ForeignKey("courses.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text)
    order = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    course = relationship("Course", back_populates="modules")
    lessons = relationship("Lesson", back_populates="module", cascade="all, delete-orphan")


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(PGUUID(as_uuid=True), primary_key=True, default=UUID)
    module_id = Column(PGUUID(as_uuid=True), ForeignKey("modules.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text)
    content = Column(Text)
    order = Column(Integer, nullable=False)
    duration = Column(Integer)  # in minutes
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    module = relationship("Module", back_populates="lessons")
    video_assets = relationship("VideoAsset", back_populates="lesson", cascade="all, delete-orphan")
    assessments = relationship("Assessment", back_populates="lesson", cascade="all, delete-orphan") 