"""
Search API endpoints.

This module provides API endpoints for searching products and companies.
"""
from typing import Dict, List, Any, Optional
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services import search as search_service

router = APIRouter()


@router.get("/products", response_model=List[Dict[str, Any]])
async def search_products(
    query: str = Query(..., description="Search query for product name or code"),
    limit: int = Query(10, description="Maximum number of results to return"),
    db: Session = Depends(get_db),
) -> List[Dict[str, Any]]:
    """
    Search for pharmaceutical products.
    
    This endpoint provides search functionality for pharmaceutical products
    based on name, code, or synonyms.
    
    Args:
        query: Search query string
        limit: Maximum number of results to return
        db: Database session
        
    Returns:
        List of matching products
    """
    try:
        return search_service.search_products(db, query, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/companies", response_model=List[Dict[str, Any]])
async def search_companies(
    query: str = Query(..., description="Search query for company name"),
    country: Optional[str] = Query(None, description="Filter by country"),
    limit: int = Query(10, description="Maximum number of results to return"),
    db: Session = Depends(get_db),
) -> List[Dict[str, Any]]:
    """
    Search for pharmaceutical companies.
    
    This endpoint provides search functionality for pharmaceutical companies
    based on name and optional country filter.
    
    Args:
        query: Search query string
        country: Optional country filter
        limit: Maximum number of results to return
        db: Database session
        
    Returns:
        List of matching companies
    """
    try:
        return search_service.search_companies(db, query, country, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/regions", response_model=List[str])
async def get_regions(
    db: Session = Depends(get_db),
) -> List[str]:
    """
    Get available regions.
    
    This endpoint provides a list of all available regions in the system.
    
    Args:
        db: Database session
        
    Returns:
        List of region names
    """
    try:
        return search_service.get_regions(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
