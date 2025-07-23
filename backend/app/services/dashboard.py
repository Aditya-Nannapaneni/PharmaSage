"""
Dashboard service.

This module provides services for the market trends dashboard.
"""
from typing import Dict, List, Any, Optional
from sqlalchemy.orm import Session

# Mock data for development
MOCK_MARKET_TRENDS = {
    "global_trade_volume": {
        "value": 847.2,
        "unit": "B",
        "currency": "USD",
        "change": 12.3,
        "trend": "up"
    },
    "active_products": {
        "value": 24567,
        "change": 847,
        "trend": "up"
    },
    "export_companies": {
        "value": 8941,
        "change": 156,
        "trend": "up"
    },
    "active_markets": {
        "value": 187,
        "change": -2,
        "trend": "down"
    },
    "regional_breakdown": [
        {"name": "North America", "volume": 127.8, "growth": 8.2, "color": "primary"},
        {"name": "Europe", "volume": 231.4, "growth": 12.1, "color": "success"},
        {"name": "Asia Pacific", "volume": 342.7, "growth": 15.3, "color": "accent"},
        {"name": "Latin America", "volume": 78.9, "growth": 6.7, "color": "warning"},
        {"name": "Africa", "volume": 44.2, "growth": 18.9, "color": "primary-glow"}
    ],
    "monthly_trends": [
        {"month": "Jan", "value": 65, "color": "bg-primary"},
        {"month": "Feb", "value": 78, "color": "bg-primary"},
        {"month": "Mar", "value": 82, "color": "bg-success"},
        {"month": "Apr", "value": 74, "color": "bg-primary"},
        {"month": "May", "value": 88, "color": "bg-success"},
        {"month": "Jun", "value": 95, "color": "bg-success"},
        {"month": "Jul", "value": 92, "color": "bg-success"},
        {"month": "Aug", "value": 87, "color": "bg-primary"},
        {"month": "Sep", "value": 94, "color": "bg-success"},
        {"month": "Oct", "value": 98, "color": "bg-success"},
        {"month": "Nov", "value": 89, "color": "bg-primary"},
        {"month": "Dec", "value": 102, "color": "bg-accent"}
    ]
}

MOCK_TOP_EXPORTERS = [
    {
        "rank": 1,
        "company": "Teva Pharmaceutical",
        "country": "Israel",
        "volume": "$72.4B",
        "marketShare": 8.5,
        "growth": "+15.2%",
        "products": ["Generic APIs", "Biosimilars", "OTC"]
    },
    {
        "rank": 2,
        "company": "Novartis",
        "country": "Switzerland",
        "volume": "$65.8B",
        "marketShare": 7.8,
        "growth": "+12.7%",
        "products": ["Oncology", "Cardiovascular", "CNS"]
    },
    {
        "rank": 3,
        "company": "Pfizer",
        "country": "United States",
        "volume": "$58.9B",
        "marketShare": 7.0,
        "growth": "+9.8%",
        "products": ["Vaccines", "Oncology", "Immunology"]
    },
    {
        "rank": 4,
        "company": "Roche",
        "country": "Switzerland",
        "volume": "$54.2B",
        "marketShare": 6.4,
        "growth": "+18.3%",
        "products": ["Diagnostics", "Oncology", "Immunology"]
    },
    {
        "rank": 5,
        "company": "Johnson & Johnson",
        "country": "United States",
        "volume": "$47.6B",
        "marketShare": 5.6,
        "growth": "+6.9%",
        "products": ["Consumer Health", "Pharmaceuticals", "Medical Devices"]
    }
]

MOCK_TOP_PRODUCTS = [
    {"rank": 1, "name": "Adalimumab", "category": "Immunology", "volume": "$21.2B", "growth": "+8.7%"},
    {"rank": 2, "name": "Apixaban", "category": "Anticoagulant", "volume": "$18.9B", "growth": "+15.3%"},
    {"rank": 3, "name": "Pembrolizumab", "category": "Oncology", "volume": "$17.2B", "growth": "+19.8%"},
    {"rank": 4, "name": "Lenalidomide", "category": "Oncology", "volume": "$12.1B", "growth": "+5.2%"},
    {"rank": 5, "name": "Ustekinumab", "category": "Immunology", "volume": "$9.3B", "growth": "+11.7%"},
    {"rank": 6, "name": "Dexamethasone", "category": "Corticosteroid", "volume": "$8.7B", "growth": "+24.5%"},
    {"rank": 7, "name": "Rituximab", "category": "Oncology", "volume": "$7.9B", "growth": "+3.1%"},
    {"rank": 8, "name": "Bevacizumab", "category": "Oncology", "volume": "$7.5B", "growth": "+2.8%"},
    {"rank": 9, "name": "Trastuzumab", "category": "Oncology", "volume": "$7.1B", "growth": "+4.2%"},
    {"rank": 10, "name": "Insulin Glargine", "category": "Diabetes", "volume": "$6.8B", "growth": "+7.9%"}
]


def get_market_trends(
    db: Session, 
    product_type: Optional[str] = None, 
    region: Optional[str] = None, 
    time_period: Optional[str] = "12m"
) -> Dict[str, Any]:
    """
    Get market trends data for the dashboard.
    
    Args:
        db: Database session
        product_type: Optional filter by product type
        region: Optional filter by geographic region
        time_period: Time period for the data
        
    Returns:
        Dict containing market trends data
    """
    # In a real implementation, this would query the database
    # For now, return mock data
    
    # Apply filters (simulated)
    data = MOCK_MARKET_TRENDS.copy()
    
    # Filter regional breakdown by region if specified
    if region:
        data["regional_breakdown"] = [r for r in data["regional_breakdown"] if r["name"] == region]
    
    return data


def get_top_exporters(
    db: Session, 
    limit: int = 5, 
    product_type: Optional[str] = None, 
    region: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Get top pharmaceutical exporters.
    
    Args:
        db: Database session
        limit: Number of exporters to return
        product_type: Optional filter by product type
        region: Optional filter by geographic region
        
    Returns:
        List of top exporters with their details
    """
    # In a real implementation, this would query the database
    # For now, return mock data
    
    # Apply filters (simulated)
    data = MOCK_TOP_EXPORTERS.copy()
    
    # Filter by country if region is specified
    if region:
        # This is a simplified mapping for demonstration
        region_country_map = {
            "North America": ["United States", "Canada", "Mexico"],
            "Europe": ["Switzerland", "Germany", "France", "United Kingdom"],
            "Asia Pacific": ["Japan", "China", "India", "Australia"],
            "Latin America": ["Brazil", "Argentina", "Colombia"],
            "Africa": ["South Africa", "Egypt", "Nigeria"]
        }
        
        countries = region_country_map.get(region, [])
        if countries:
            data = [e for e in data if e["country"] in countries]
    
    # Limit the results
    return data[:limit]


def get_top_products(
    db: Session, 
    limit: int = 10, 
    region: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Get top pharmaceutical products.
    
    Args:
        db: Database session
        limit: Number of products to return
        region: Optional filter by geographic region
        
    Returns:
        List of top products with their details
    """
    # In a real implementation, this would query the database
    # For now, return mock data
    
    # Apply filters (simulated)
    data = MOCK_TOP_PRODUCTS.copy()
    
    # Limit the results
    return data[:limit]
