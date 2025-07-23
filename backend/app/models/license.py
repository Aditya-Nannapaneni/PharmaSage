"""
License model.

This module defines the License model for storing pharmaceutical product licenses.
"""
from sqlalchemy import Column, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base, TimestampMixin, UUIDMixin


class License(Base, UUIDMixin, TimestampMixin):
    """
    License model.
    
    Represents a pharmaceutical product license or market authorization in the system.
    """
    
    # License details
    region = Column(String(100), nullable=False, index=True)
    exp_date = Column(Date, nullable=True)
    status = Column(String(50), nullable=False, index=True)  # active, expired, pending, etc.
    
    # Additional information
    license_number = Column(String(100), nullable=True)
    authority = Column(String(100), nullable=True)
    
    # Foreign keys
    company_id = Column(UUID(as_uuid=True), ForeignKey("company.id"), nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"), nullable=False)
    
    # Relationships
    company = relationship("Company", back_populates="licenses")
    product = relationship("Product", back_populates="licenses")
    
    def __repr__(self) -> str:
        """String representation of the license."""
        return f"<License {self.region} for {self.product_id} ({self.status})>"
