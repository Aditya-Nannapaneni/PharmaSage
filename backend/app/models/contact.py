"""
Contact model.

This module defines the Contact model for storing contact information for pharmaceutical companies.
"""
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base, TimestampMixin, UUIDMixin


class Contact(Base, UUIDMixin, TimestampMixin):
    """
    Contact model.
    
    Represents a contact person at a pharmaceutical company.
    """
    
    # Contact details
    name = Column(String(255), nullable=False, index=True)
    role = Column(String(255), nullable=False, index=True)
    linkedin_url = Column(String(255), nullable=True)
    
    # Additional information
    email = Column(String(255), nullable=True)
    phone = Column(String(100), nullable=True)
    department = Column(String(100), nullable=True, index=True)
    seniority = Column(String(50), nullable=True, index=True)
    
    # Notes and metadata
    notes = Column(Text, nullable=True)
    relationship_score = Column(String(50), nullable=True)
    last_interaction = Column(String(100), nullable=True)
    
    # Foreign keys
    company_id = Column(UUID(as_uuid=True), ForeignKey("company.id"), nullable=False)
    
    # Relationships
    company = relationship("Company", back_populates="contacts")
    
    def __repr__(self) -> str:
        """String representation of the contact."""
        return f"<Contact {self.name} ({self.role}) at {self.company_id}>"
