"""
Transaction model.

This module defines the Transaction model for storing pharmaceutical trade transactions.
"""
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base, TimestampMixin, UUIDMixin


class Transaction(Base, UUIDMixin, TimestampMixin):
    """
    Transaction model.
    
    Represents a pharmaceutical trade transaction (import/export) in the system.
    """
    
    # Transaction details
    year = Column(Integer, nullable=False, index=True)
    month = Column(Integer, nullable=True, index=True)
    qty = Column(Float, nullable=True)
    value = Column(Float, nullable=True)
    flow_type = Column(String(50), nullable=False, index=True)  # export/import
    
    # Geographic information
    source_country = Column(String(100), nullable=False, index=True)
    destination_country = Column(String(100), nullable=False, index=True)
    
    # Additional information
    customs_proc_code = Column(String(100), nullable=True)
    mode_of_transport = Column(String(100), nullable=True)
    
    # Foreign keys
    company_id = Column(UUID(as_uuid=True), ForeignKey("company.id"), nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"), nullable=False)
    
    # Relationships
    company = relationship("Company", back_populates="transactions")
    product = relationship("Product", back_populates="transactions")
    
    def __repr__(self) -> str:
        """String representation of the transaction."""
        return f"<Transaction {self.flow_type} {self.source_country}->{self.destination_country} ({self.year}-{self.month or 'XX'})>"
