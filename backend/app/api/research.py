"""
Research API endpoints.

This module provides API endpoints for the research functionality.
"""
from typing import Dict, List, Any, Optional
from fastapi import APIRouter, Depends, Body, Query, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services import buyer_research
from app.core.config import settings

router = APIRouter()


@router.post("/buyers", response_model=List[Dict[str, Any]])
async def research_buyers(
    company_name: str = Body(..., description="Company name"),
    company_website: str = Body(..., description="Company website URL"),
    products: List[str] = Body(..., description="List of product names"),
    db: Session = Depends(get_db),
) -> List[Dict[str, Any]]:
    """
    Research potential buyers for a company using AI-powered deep research.
    
    This endpoint analyzes the company website and market data to identify
    potential buyers for the company's products.
    
    Args:
        company_name: Name of the company
        company_website: Website URL of the company
        products: List of product names
        db: Database session
        
    Returns:
        List of potential buyer prospects with details
    """
    try:
        return buyer_research.research_potential_buyers(
            db, company_name, company_website, products
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
        "status": "available" if settings.PERPLEXITY_API_KEY else "unconfigured",
        "message": "Research service is ready" if settings.PERPLEXITY_API_KEY else "API key not configured"
    }
    
    return status
