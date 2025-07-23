"""
Database session management.

This module provides utilities for creating database sessions and engines.
"""
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.core.config import settings

# Create SQLAlchemy engine
# Convert PostgresDsn to string before passing to create_engine
engine = create_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),  # Convert to string
    pool_pre_ping=True,  # Check connection before using it
    pool_size=10,        # Maximum number of connections in the pool
    max_overflow=20,     # Maximum number of connections that can be created beyond pool_size
    pool_recycle=3600,   # Recycle connections after 1 hour
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """
    Get a database session.
    
    This function creates a new database session and ensures it is closed
    after use, even if an exception occurs.
    
    Yields:
        Session: A SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
