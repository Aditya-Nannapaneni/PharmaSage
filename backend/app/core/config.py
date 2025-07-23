"""
Configuration settings for the PharmaSage backend.

This module contains the settings for the application, including:
- Project information
- Database connection
- API keys and secrets
- CORS settings
- Other configuration parameters
"""
import os
import secrets
from typing import Any, List, Optional, Union

from pydantic import AnyHttpUrl, PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""
    
    # Project information
    PROJECT_NAME: str = "PharmaSage"
    PROJECT_DESCRIPTION: str = "Pharmaceutical Business Intelligence Platform"
    PROJECT_VERSION: str = "0.1.0"
    
    # API settings
    API_V1_STR: str = "/api"
    
    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # CORS
    CORS_ORIGINS: List[Union[str, AnyHttpUrl]] = ["http://localhost:5173", "http://localhost:8000"]
    
    # Database
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "pharmasage")
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    def assemble_db_connection(cls, v: Optional[str], info: Any) -> Any:
        if isinstance(v, str):
            return v
        
        # Get values from the model's fields
        postgres_server = cls.model_fields["POSTGRES_SERVER"].default
        postgres_user = cls.model_fields["POSTGRES_USER"].default
        postgres_password = cls.model_fields["POSTGRES_PASSWORD"].default
        postgres_db = cls.model_fields["POSTGRES_DB"].default
        
        # Use environment variables if available
        postgres_server = os.getenv("POSTGRES_SERVER", postgres_server)
        postgres_user = os.getenv("POSTGRES_USER", postgres_user)
        postgres_password = os.getenv("POSTGRES_PASSWORD", postgres_password)
        postgres_db = os.getenv("POSTGRES_DB", postgres_db)
        
        return PostgresDsn.build(
            scheme="postgresql",
            username=postgres_user,
            password=postgres_password,
            host=postgres_server,
            path=f"{postgres_db or ''}",
        )
    
    # S3 Data Lake
    S3_BUCKET_NAME: str = os.getenv("S3_BUCKET_NAME", "pharmasage-data-lake")
    AWS_ACCESS_KEY_ID: Optional[str] = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: Optional[str] = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION: str = os.getenv("AWS_REGION", "us-east-1")
    
    # Anthropic API
    ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    
    # Redis Cache (optional)
    REDIS_HOST: Optional[str] = os.getenv("REDIS_HOST")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379"))
    
    # Model config
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


# Create settings instance
settings = Settings()
