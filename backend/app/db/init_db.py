"""
Database initialization.

This module provides functions to initialize the database, create tables,
and populate initial data.
"""
import logging
from sqlalchemy.orm import Session

from app.db.base import Base
from app.db.session import engine
from app.core.config import settings

# Import all models to ensure they are registered with SQLAlchemy
from app.models.company import Company
from app.models.product import Product
from app.models.transaction import Transaction
from app.models.license import License
from app.models.contact import Contact

logger = logging.getLogger(__name__)


def init_db() -> None:
    """
    Initialize the database.
    
    This function creates all tables and populates initial data if needed.
    """
    # Create tables
    logger.info("Creating database tables")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created")


def seed_initial_data(db: Session) -> None:
    """
    Seed the database with initial data.
    
    This function populates the database with initial data for testing and development.
    
    Args:
        db: Database session
    """
    # Check if database is already seeded
    if db.query(Company).count() > 0:
        logger.info("Database already contains data, skipping seeding")
        return

    logger.info("Seeding database with initial data")
    
    # Add seed data here
    # Example:
    # db.add(Company(name="Example Company", country="US"))
    # db.commit()
    
    logger.info("Database seeded successfully")
