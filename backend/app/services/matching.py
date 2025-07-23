"""
Matching service.

This module provides services for the prospect matching functionality.
"""
from typing import Dict, List, Any, Optional
import uuid
from sqlalchemy.orm import Session

# Mock data for development
MOCK_PROSPECTS = [
    {
        "id": "1",
        "name": "MedCore Pharmaceuticals",
        "location": "Berlin, Germany",
        "segment": "Generic Medications",
        "revenue": "$2.4B",
        "employees": "5,000-10,000",
        "purchasingVolume": "$180M",
        "opportunityScore": 92,
        "status": "Hot Lead",
        "lastContact": "2 days ago",
        "keyProducts": ["Antibiotics", "Pain Relief", "Cardiovascular"]
    },
    {
        "id": "2",
        "name": "BioPharma Solutions",
        "location": "São Paulo, Brazil",
        "segment": "Specialty Drugs",
        "revenue": "$890M",
        "employees": "1,000-5,000",
        "purchasingVolume": "$65M",
        "opportunityScore": 78,
        "status": "Qualified",
        "lastContact": "1 week ago",
        "keyProducts": ["Oncology", "Immunology", "Rare Diseases"]
    },
    {
        "id": "3",
        "name": "Global Health Networks",
        "location": "Mumbai, India",
        "segment": "Distribution",
        "revenue": "$1.2B",
        "employees": "2,000-5,000",
        "purchasingVolume": "$95M",
        "opportunityScore": 85,
        "status": "Research",
        "lastContact": "3 days ago",
        "keyProducts": ["Vaccines", "Generic Drugs", "Medical Devices"]
    },
    {
        "id": "4",
        "name": "PharmaVision Corp",
        "location": "Toronto, Canada",
        "segment": "Research & Development",
        "revenue": "$450M",
        "employees": "500-1,000",
        "purchasingVolume": "$28M",
        "opportunityScore": 71,
        "status": "New Lead",
        "lastContact": "5 days ago",
        "keyProducts": ["Clinical Trials", "Drug Development", "Biomarkers"]
    },
    {
        "id": "5",
        "name": "MediTech Innovations",
        "location": "Tokyo, Japan",
        "segment": "Medical Devices",
        "revenue": "$780M",
        "employees": "1,000-5,000",
        "purchasingVolume": "$42M",
        "opportunityScore": 68,
        "status": "New Lead",
        "lastContact": "1 week ago",
        "keyProducts": ["Diagnostic Equipment", "Surgical Tools", "Monitoring Devices"]
    }
]

MOCK_PROSPECT_DETAILS = {
    "1": {
        "id": "1",
        "name": "MedCore Pharmaceuticals",
        "location": "Berlin, Germany",
        "segment": "Generic Medications",
        "revenue": "$2.4B",
        "employees": "5,000-10,000",
        "purchasingVolume": "$180M",
        "opportunityScore": 92,
        "status": "Hot Lead",
        "lastContact": "2 days ago",
        "keyProducts": ["Antibiotics", "Pain Relief", "Cardiovascular"],
        "description": "MedCore Pharmaceuticals is a leading manufacturer of generic medications in Europe, with a strong focus on antibiotics and cardiovascular drugs. The company has been expanding its international presence and is actively seeking new suppliers for APIs.",
        "tradingHistory": [
            {"year": 2023, "volume": "$175M", "growth": "+12%"},
            {"year": 2022, "volume": "$156M", "growth": "+8%"},
            {"year": 2021, "volume": "$144M", "growth": "+5%"}
        ],
        "complianceStatus": {
            "rating": "High",
            "certifications": ["EU GMP", "ISO 9001", "ISO 14001"],
            "lastAudit": "March 2023",
            "issues": []
        },
        "marketPresence": ["Germany", "France", "UK", "Italy", "Spain", "Poland", "Netherlands"],
        "competitors": ["Teva", "Sandoz", "Mylan"]
    },
    "2": {
        "id": "2",
        "name": "BioPharma Solutions",
        "location": "São Paulo, Brazil",
        "segment": "Specialty Drugs",
        "revenue": "$890M",
        "employees": "1,000-5,000",
        "purchasingVolume": "$65M",
        "opportunityScore": 78,
        "status": "Qualified",
        "lastContact": "1 week ago",
        "keyProducts": ["Oncology", "Immunology", "Rare Diseases"],
        "description": "BioPharma Solutions is a rapidly growing specialty pharmaceutical company focused on oncology and immunology treatments. The company has a strong presence in Latin America and is expanding into North America and Europe.",
        "tradingHistory": [
            {"year": 2023, "volume": "$65M", "growth": "+18%"},
            {"year": 2022, "volume": "$55M", "growth": "+22%"},
            {"year": 2021, "volume": "$45M", "growth": "+15%"}
        ],
        "complianceStatus": {
            "rating": "Medium",
            "certifications": ["ANVISA", "ISO 9001"],
            "lastAudit": "November 2022",
            "issues": ["Documentation gaps in one facility (resolved)"]
        },
        "marketPresence": ["Brazil", "Argentina", "Colombia", "Mexico", "Chile"],
        "competitors": ["EMS Pharma", "Eurofarma", "Libbs"]
    }
}

MOCK_GUIDANCE = {
    "talkingPoints": [
        "MedCore's expansion into cardiovascular treatments aligns with our API portfolio",
        "Recent EU regulatory changes have created supply chain challenges they're looking to solve",
        "Their purchasing volume increased 12% last year, indicating growth in production capacity",
        "They're actively seeking reliable suppliers with strong quality control processes"
    ],
    "decisionMakers": [
        {
            "name": "Dr. Sarah Chen",
            "title": "Chief Procurement Officer",
            "influence": "Primary decision maker for API sourcing",
            "interests": "Supply chain resilience, quality consistency, competitive pricing"
        },
        {
            "name": "Thomas Weber",
            "title": "Head of R&D",
            "influence": "Technical evaluator for new suppliers",
            "interests": "API purity profiles, stability data, manufacturing processes"
        }
    ],
    "outreachStrategy": {
        "recommendedApproach": "Technical value proposition focused on quality and supply reliability",
        "keyDifferentiators": [
            "Our EU-GMP certified manufacturing facilities",
            "Consistent 99.8% purity profile exceeding industry standards",
            "Guaranteed supply chain redundancy with multiple production sites"
        ],
        "nextSteps": [
            "Send technical documentation package to Dr. Chen",
            "Request technical evaluation meeting with R&D team",
            "Offer facility virtual tour to demonstrate quality processes"
        ]
    }
}


def find_prospects(
    db: Session, 
    company_name: str, 
    products: List[str], 
    licensed_markets: List[str], 
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Find potential buyer prospects.
    
    Args:
        db: Database session
        company_name: Name of the company
        products: List of product names or IDs
        licensed_markets: List of licensed markets
        limit: Maximum number of prospects to return
        
    Returns:
        List of potential buyer prospects with details
    """
    # In a real implementation, this would query the database and run a matching algorithm
    # For now, return mock data
    
    # Simulate filtering based on licensed markets
    results = []
    for prospect in MOCK_PROSPECTS:
        # In a real implementation, we would check if the prospect operates in any of the licensed markets
        # For now, just return all prospects
        results.append(prospect)
    
    # Sort by opportunity score (descending)
    results.sort(key=lambda x: x["opportunityScore"], reverse=True)
    
    # Limit the results
    return results[:limit]


def get_prospect_details(
    db: Session, 
    prospect_id: str
) -> Dict[str, Any]:
    """
    Get detailed information about a prospect.
    
    Args:
        db: Database session
        prospect_id: ID of the prospect
        
    Returns:
        Detailed prospect information
    """
    # In a real implementation, this would query the database
    # For now, return mock data
    
    # Check if we have detailed information for this prospect
    if prospect_id in MOCK_PROSPECT_DETAILS:
        return MOCK_PROSPECT_DETAILS[prospect_id]
    
    # If not, find the prospect in the basic list
    for prospect in MOCK_PROSPECTS:
        if prospect["id"] == prospect_id:
            # Return basic information
            return prospect
    
    # If prospect not found, return empty dict
    return {}


def generate_outreach_guidance(
    db: Session, 
    prospect_id: str, 
    company_id: str, 
    products: List[str]
) -> Dict[str, Any]:
    """
    Generate AI-powered outreach guidance.
    
    Args:
        db: Database session
        prospect_id: ID of the prospect
        company_id: ID of the user's company
        products: List of product names or IDs
        
    Returns:
        Outreach guidance and talking points
    """
    # In a real implementation, this would use the Anthropic API to generate guidance
    # For now, return mock data
    
    # Get prospect details
    prospect = get_prospect_details(db, prospect_id)
    
    # If prospect not found, return empty guidance
    if not prospect:
        return {
            "talkingPoints": [],
            "decisionMakers": [],
            "outreachStrategy": {
                "recommendedApproach": "",
                "keyDifferentiators": [],
                "nextSteps": []
            }
        }
    
    # For now, return mock guidance
    return MOCK_GUIDANCE
