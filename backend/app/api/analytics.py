"""
Analytics API endpoints.

This module provides API endpoints for tracking usage metrics.
"""
from typing import Dict, List, Any, Optional
from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services import analytics as analytics_service

router = APIRouter()


@router.post("/event", response_model=Dict[str, str])
async def track_event(
    event_type: str = Body(..., description="Type of event to track"),
    event_data: Dict[str, Any] = Body({}, description="Event data"),
    db: Session = Depends(get_db),
) -> Dict[str, str]:
    """
    Track a usage event.
    
    This endpoint tracks a usage event in the system.
    
    Args:
        event_type: Type of event to track
        event_data: Event data
        db: Database session
        
    Returns:
        Confirmation message
    """
    try:
        analytics_service.track_event(db, event_type, event_data)
        return {"status": "success", "message": "Event tracked successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/metrics", response_model=Dict[str, Any])
async def get_metrics(
    metric_type: str,
    time_period: str = "7d",
    db: Session = Depends(get_db),
) -> Dict[str, Any]:
    """
    Get usage metrics.
    
    This endpoint retrieves usage metrics from the system.
    
    Args:
        metric_type: Type of metrics to retrieve
        time_period: Time period for the metrics (1d, 7d, 30d, 90d)
        db: Database session
        
    Returns:
        Usage metrics
    """
    try:
        return analytics_service.get_metrics(db, metric_type, time_period)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/popular-searches", response_model=List[Dict[str, Any]])
async def get_popular_searches(
    limit: int = 10,
    db: Session = Depends(get_db),
) -> List[Dict[str, Any]]:
    """
    Get popular searches.
    
    This endpoint retrieves the most popular searches in the system.
    
    Args:
        limit: Maximum number of searches to return
        db: Database session
        
    Returns:
        List of popular searches
    """
    try:
        return analytics_service.get_popular_searches(db, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
