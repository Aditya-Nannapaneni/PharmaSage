"""
Company model.

This module defines the Company model for storing company information.
"""
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

from app.db.base import Base, TimestampMixin, UUIDMixin


class Company(Base, UUIDMixin, TimestampMixin):
    """
    Company model.
    
    Represents a pharmaceutical company in the system.
    """
    
    # Basic information
    name = Column(String(255), nullable=False, index=True)
    country = Column(String(100), nullable=False, index=True)
    registry_id = Column(String(100), nullable=True)
    sector = Column(String(100), nullable=True)
    size = Column(String(50), nullable=True)
    
    # Additional information
    description = Column(Text, nullable=True)
    website = Column(String(255), nullable=True)
    
    # Relationships
    products = relationship("Product", back_populates="company", cascade="all, delete-orphan")
    transactions = relationship("Transaction", back_populates="company", cascade="all, delete-orphan")
    licenses = relationship("License", back_populates="company", cascade="all, delete-orphan")
    contacts = relationship("Contact", back_populates="company", cascade="all, delete-orphan")
    
    def __repr__(self) -> str:
        """String representation of the company."""
        return f"<Company {self.name} ({self.country})>"
