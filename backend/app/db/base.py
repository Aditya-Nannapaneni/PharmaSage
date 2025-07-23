"""
SQLAlchemy Base class for all models.

This module defines the Base class that all SQLAlchemy models will inherit from.
It also includes common mixins and utilities for models.
"""
from typing import Any, Dict
from datetime import datetime
import uuid

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    """Base class for all models."""
    
    id: Any
    __name__: str
    
    # Generate __tablename__ automatically based on class name
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class TimestampMixin:
    """Mixin to add created_at and updated_at columns to models."""
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class UUIDMixin:
    """Mixin to add UUID primary key to models."""
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
