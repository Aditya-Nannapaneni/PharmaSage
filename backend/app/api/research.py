"""
Research API endpoints.

This module provides API endpoints for the research functionality.
"""
from typing import Dict, List, Any, Optional
from fastapi import APIRouter, Depends, Body, Query, HTTPException
from sqlalchemy.orm import Session
from urllib.parse import urlparse

from app.db.session import get_db
from app.services import buyer_research
from app.core.config import settings

router = APIRouter()


def validate_url(url: str) -> bool:
    """
    Validate if the provided string is a proper URL.
    
    Args:
        url: The URL string to validate
        
    Returns:
        True if the URL is valid, False otherwise
    """
    try:
        result = urlparse(url)
        return all([result.scheme in ['http', 'https'], result.netloc])
    except:
        return False


@router.post("/buyers", response_model=Dict[str, Any])
async def research_buyers(
    company_name: str = Body(..., description="Company name"),
    company_website: str = Body(..., description="Company website URL"),
    db: Session = Depends(get_db),
) -> Dict[str, Any]:
    """
    Research potential buyers for a company using AI-powered deep research.
    
    This endpoint analyzes the company website and market data to identify
    potential buyers for the company's products.
    
    Args:
        company_name: Name of the company
        company_website: Website URL of the company
        db: Database session
        
    Returns:
        Dictionary with source company info, ideal customer profile, and discovered buyers
    """
    # Validate the URL
    if not validate_url(company_website):
        raise HTTPException(
            status_code=400, 
            detail="Invalid URL format. Please provide a valid URL (e.g., https://example.com)"
        )
    
    try:
        return buyer_research.research_potential_buyers(
            db, company_name, company_website
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/status", response_model=Dict[str, Any])
async def check_research_status() -> Dict[str, Any]:
    """
    Check the status of the research service.
    
    This endpoint verifies that the research service is properly configured
    and available.
    
    Returns:
        Status information about the research service
    """
    status = {
        "service": "research",
        "status": "available" if settings.PERPLEXITY_API_KEY or settings.USE_MOCK_RESPONSES else "unconfigured",
        "mode": "mock" if settings.USE_MOCK_RESPONSES else "live",
        "api_configured": settings.PERPLEXITY_API_KEY is not None,
        "message": "Research service is ready" if settings.PERPLEXITY_API_KEY or settings.USE_MOCK_RESPONSES else "API key not configured"
    }
    
    return status
