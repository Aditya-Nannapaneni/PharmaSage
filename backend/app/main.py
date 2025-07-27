"""
PharmaSage Backend API

This is the main entry point for the PharmaSage backend API.
It initializes the FastAPI application and includes all routers.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
import logging

from app.api import dashboard, search, match, contacts, export, analytics, research
from app.core.config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["dashboard"])
app.include_router(search.router, prefix="/api/search", tags=["search"])
app.include_router(match.router, prefix="/api/match", tags=["match"])
app.include_router(contacts.router, prefix="/api/prospect", tags=["contacts"])
app.include_router(export.router, prefix="/api/export", tags=["export"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])
app.include_router(research.router, prefix="/api/research", tags=["research"])

# Mount static files (for frontend in integrated deployment)
# Check for dist directory in both current directory and parent directory
dist_path = "dist"
if not os.path.exists(dist_path):
    # Try parent directory
    parent_dist_path = os.path.join("..", "dist")
    if os.path.exists(parent_dist_path):
        dist_path = parent_dist_path
        logger.info(f"Using dist directory from parent directory: {os.path.abspath(parent_dist_path)}")

if os.path.exists(dist_path):
    logger.info(f"Mounting static files from: {os.path.abspath(dist_path)}")
    app.mount("/", StaticFiles(directory=dist_path, html=True), name="static")
else:
    logger.warning("No dist directory found. Static files will not be served.")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
