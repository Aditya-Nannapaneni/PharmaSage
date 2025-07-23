"""
Analytics service.

This module provides services for tracking usage metrics.
"""
from typing import Dict, List, Any, Optional
from datetime import datetime
from sqlalchemy.orm import Session

# Mock data for development
MOCK_METRICS = {
    "search_volume": {
        "1d": 124,
        "7d": 876,
        "30d": 3245,
        "90d": 9876
    },
    "export_volume": {
        "1d": 18,
        "7d": 97,
        "30d": 342,
        "90d": 1245
    },
    "prospect_matches": {
        "1d": 45,
        "7d": 287,
        "30d": 1124,
        "90d": 3567
    },
    "user_engagement": {
        "1d": 87,
        "7d": 543,
        "30d": 2134,
        "90d": 6789
    }
}

MOCK_POPULAR_SEARCHES = [
    {"query": "paracetamol", "count": 156, "last_search": "2 hours ago"},
    {"query": "antibiotics", "count": 124, "last_search": "30 minutes ago"},
    {"query": "oncology", "count": 98, "last_search": "1 hour ago"},
    {"query": "vaccines", "count": 87, "last_search": "45 minutes ago"},
    {"query": "insulin", "count": 76, "last_search": "3 hours ago"},
    {"query": "cardiovascular", "count": 65, "last_search": "2 hours ago"},
    {"query": "immunology", "count": 54, "last_search": "1 day ago"},
    {"query": "generics", "count": 43, "last_search": "4 hours ago"},
    {"query": "biosimilars", "count": 32, "last_search": "5 hours ago"},
    {"query": "rare diseases", "count": 21, "last_search": "2 days ago"}
]


def track_event(
    db: Session, 
    event_type: str, 
    event_data: Dict[str, Any]
) -> None:
    """
    Track a usage event.
    
    Args:
        db: Database session
        event_type: Type of event to track
        event_data: Event data
    """
    # In a real implementation, this would store the event in the database
    # For now, just log it
    print(f"[{datetime.now().isoformat()}] Event: {event_type}, Data: {event_data}")


def get_metrics(
    db: Session, 
    metric_type: str, 
    time_period: str = "7d"
) -> Dict[str, Any]:
    """
    Get usage metrics.
    
    Args:
        db: Database session
        metric_type: Type of metrics to retrieve
        time_period: Time period for the metrics (1d, 7d, 30d, 90d)
        
    Returns:
        Usage metrics
    """
    # In a real implementation, this would query the database
    # For now, return mock data
    
    # Check if the metric type exists
    if metric_type in MOCK_METRICS:
        # Check if the time period exists
        if time_period in MOCK_METRICS[metric_type]:
            return {
                "metric_type": metric_type,
                "time_period": time_period,
                "value": MOCK_METRICS[metric_type][time_period],
                "timestamp": datetime.now().isoformat()
            }
    
    # If metric type or time period not found, return empty dict
    return {
        "metric_type": metric_type,
        "time_period": time_period,
        "value": 0,
        "timestamp": datetime.now().isoformat()
    }


def get_popular_searches(
    db: Session, 
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Get popular searches.
    
    Args:
        db: Database session
        limit: Maximum number of searches to return
        
    Returns:
        List of popular searches
    """
    # In a real implementation, this would query the database
    # For now, return mock data
    return MOCK_POPULAR_SEARCHES[:limit]
