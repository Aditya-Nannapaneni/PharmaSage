"""
Product model.

This module defines the Product model for storing pharmaceutical product information.
"""
from sqlalchemy import Column, String, Text, ARRAY, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base, TimestampMixin, UUIDMixin


class Product(Base, UUIDMixin, TimestampMixin):
    """
    Product model.
    
    Represents a pharmaceutical product (drug/API) in the system.
    """
    
    # Basic information
    api_name = Column(String(255), nullable=False, index=True)
    synonyms = Column(ARRAY(String), nullable=True)
    code = Column(String(100), nullable=True, index=True)
    form = Column(String(100), nullable=True)
    
    # Additional information
    description = Column(Text, nullable=True)
    therapeutic_category = Column(String(100), nullable=True, index=True)
    
    # Foreign keys
    company_id = Column(UUID(as_uuid=True), ForeignKey("company.id"), nullable=True)
    
    # Relationships
    company = relationship("Company", back_populates="products")
    transactions = relationship("Transaction", back_populates="product", cascade="all, delete-orphan")
    licenses = relationship("License", back_populates="product", cascade="all, delete-orphan")
    
    def __repr__(self) -> str:
        """String representation of the product."""
        return f"<Product {self.api_name} ({self.form or 'N/A'})>"
