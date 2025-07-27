"""
Match API endpoints.

This module provides API endpoints for the prospect matching functionality.
"""
from typing import Dict, List, Any, Optional
import logging
from fastapi import APIRouter, Depends, Body, Query, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services import matching as matching_service

# Configure logging
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/prospects", response_model=List[Dict[str, Any]])
async def find_prospects(
    company_name: str = Body(..., description="Company name"),
    products: List[str] = Body(..., description="List of product names or IDs"),
    licensed_markets: List[str] = Body(..., description="List of licensed markets"),
    limit: int = Body(10, description="Maximum number of prospects to return"),
    use_deep_research: bool = Body(False, description="Whether to use AI-powered deep research"),
    company_website: Optional[str] = Body(None, description="Company website URL (required if use_deep_research is True)"),
    db: Session = Depends(get_db),
) -> List[Dict[str, Any]]:
    """
    Find potential buyer prospects.
    
    This endpoint analyzes the input company, products, and licensed markets
    to identify potential buyers across the supplied markets.
    
    Args:
        company_name: Name of the company
        products: List of product names or IDs
        licensed_markets: List of licensed markets
        limit: Maximum number of prospects to return
        use_deep_research: Whether to use AI-powered deep research
        company_website: Company website URL (required if use_deep_research is True)
        db: Database session
        
    Returns:
        List of potential buyer prospects with details
    """
    try:
        # Debug log the input parameters
        logger.info(f"API call: find_prospects with use_deep_research={use_deep_research}, company_website={company_website}")
        
        # Validate that company_website is provided if use_deep_research is True
        if use_deep_research and not company_website:
            raise HTTPException(
                status_code=400, 
                detail="Company website URL is required when using deep research"
            )
            
        # Call the service function
        results = matching_service.find_prospects(
            db, 
            company_name, 
            products, 
            licensed_markets, 
            limit,
            use_deep_research,
            company_website
        )
        
        # Debug log the results
        logger.info(f"API result: {len(results)} prospects")
        
        return results
    except Exception as e:
        logger.error(f"API error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/prospect/{prospect_id}", response_model=Dict[str, Any])
async def get_prospect_details(
    prospect_id: str,
    db: Session = Depends(get_db),
) -> Dict[str, Any]:
    """
    Get detailed information about a prospect.
    
    This endpoint provides detailed information about a specific prospect,
    including company profile, trade activity, and compliance status.
    
    Args:
        prospect_id: ID of the prospect
        db: Database session
        
    Returns:
        Detailed prospect information
    """
    try:
        return matching_service.get_prospect_details(db, prospect_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/guidance", response_model=Dict[str, Any])
async def generate_outreach_guidance(
    prospect_id: str = Body(..., description="ID of the prospect"),
    company_id: str = Body(..., description="ID of the user's company"),
    products: List[str] = Body(..., description="List of product names or IDs"),
    db: Session = Depends(get_db),
) -> Dict[str, Any]:
    """
    Generate AI-powered outreach guidance.
    
    This endpoint uses AI to generate guidance for reaching out to a prospect,
    including talking points and outreach strategies.
    
    Args:
        prospect_id: ID of the prospect
        company_id: ID of the user's company
        products: List of product names or IDs
        db: Database session
        
    Returns:
        Outreach guidance and talking points
    """
    try:
        return matching_service.generate_outreach_guidance(db, prospect_id, company_id, products)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
