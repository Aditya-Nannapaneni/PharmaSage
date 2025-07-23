"""
Dashboard API endpoints.

This module provides API endpoints for the market trends dashboard.
"""
from typing import Dict, List, Any, Optional
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services import dashboard as dashboard_service

router = APIRouter()


@router.get("/trends", response_model=Dict[str, Any])
async def get_market_trends(
    product_type: Optional[str] = Query(None, description="Filter by product type (API/FDF)"),
    region: Optional[str] = Query(None, description="Filter by geographic region"),
    time_period: Optional[str] = Query("12m", description="Time period (1m, 3m, 6m, 12m, 2y)"),
    db: Session = Depends(get_db),
) -> Dict[str, Any]:
    """
    Get market trends data for the dashboard.
    
    This endpoint provides aggregated data for the market trends dashboard,
    including global trade volumes, growth rates, and regional breakdowns.
    
    Args:
        product_type: Optional filter by product type
        region: Optional filter by geographic region
        time_period: Time period for the data
        db: Database session
        
    Returns:
        Dict containing market trends data
    """
    try:
        return dashboard_service.get_market_trends(db, product_type, region, time_period)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/top-exporters", response_model=List[Dict[str, Any]])
async def get_top_exporters(
    limit: int = Query(5, description="Number of exporters to return"),
    product_type: Optional[str] = Query(None, description="Filter by product type"),
    region: Optional[str] = Query(None, description="Filter by geographic region"),
    db: Session = Depends(get_db),
) -> List[Dict[str, Any]]:
    """
    Get top pharmaceutical exporters.
    
    This endpoint provides a list of top pharmaceutical exporters
    based on trade volume, with optional filtering.
    
    Args:
        limit: Number of exporters to return
        product_type: Optional filter by product type
        region: Optional filter by geographic region
        db: Database session
        
    Returns:
        List of top exporters with their details
    """
    try:
        return dashboard_service.get_top_exporters(db, limit, product_type, region)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/top-products", response_model=List[Dict[str, Any]])
async def get_top_products(
    limit: int = Query(10, description="Number of products to return"),
    region: Optional[str] = Query(None, description="Filter by geographic region"),
    db: Session = Depends(get_db),
) -> List[Dict[str, Any]]:
    """
    Get top pharmaceutical products.
    
    This endpoint provides a list of top pharmaceutical products
    based on trade volume, with optional filtering.
    
    Args:
        limit: Number of products to return
        region: Optional filter by geographic region
        db: Database session
        
    Returns:
        List of top products with their details
    """
    try:
        return dashboard_service.get_top_products(db, limit, region)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
