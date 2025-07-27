"""
Matching service.

This module provides services for the prospect matching functionality.
"""
from typing import Dict, List, Any, Optional
import uuid
import logging
from sqlalchemy.orm import Session

# Configure logging
logger = logging.getLogger(__name__)

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
    limit: int = 10,
    use_deep_research: bool = False,
    company_website: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Find potential buyer prospects.
    
    Args:
        db: Database session
        company_name: Name of the company
        products: List of product names or IDs
        licensed_markets: List of licensed markets
        limit: Maximum number of prospects to return
        use_deep_research: Whether to use Perplexity Deep Research
        company_website: Website URL of the company (required if use_deep_research is True)
        
    Returns:
        List of potential buyer prospects with details
    """
    results = []
    
    # If deep research is requested and we have a company website
    if use_deep_research and company_website:
        try:
            # Import here to avoid circular imports
            from app.services import buyer_research
            
            logger.info(f"Using deep research for {company_name} ({company_website})")
            
            # Get research-based prospects
            research_results = buyer_research.research_potential_buyers(
                db, company_name, company_website, products
            )
            
            # Debug log the research results
            logger.info(f"Research results: {research_results}")
            
            # Add research results to the list
            results.extend(research_results)
            
            logger.info(f"Found {len(research_results)} prospects through deep research")
            logger.info(f"Results after adding research: {len(results)} prospects")
        except Exception as e:
            # Log the error but continue with the regular matching
            logger.error(f"Deep research failed: {str(e)}")
    
    # Continue with the existing implementation
    logger.info("Adding database/mock prospects")
    for prospect in MOCK_PROSPECTS:
        # In a real implementation, we would check if the prospect operates in any of the licensed markets
        # For now, just return all prospects
        results.append(prospect)
    
    logger.info(f"Results after adding mock: {len(results)} prospects")
    
    # Sort by opportunity score (descending)
    results.sort(key=lambda x: x["opportunityScore"], reverse=True)
    
    # Limit the results
    limited_results = results[:limit]
    logger.info(f"Final results after limiting: {len(limited_results)} prospects")
    
    return limited_results


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
    logger.info(f"Getting details for prospect: {prospect_id}")
    
    # In a real implementation, this would query the database
    # For now, return mock data
    
    # Check if this is a research-based prospect
    if prospect_id.startswith("research-"):
        logger.info("This is a research-based prospect")
        
        # For research-based prospects, we need to get the data from the research service
        try:
            # Import here to avoid circular imports
            from app.services import buyer_research
            
            # Get research-based prospects
            research_results = buyer_research.research_potential_buyers(
                db, "Example Pharma", "https://example.com", ["Product A", "Product B"]
            )
            
            # Find the prospect with the matching ID
            for prospect in research_results:
                if prospect["id"] == prospect_id:
                    logger.info(f"Found research-based prospect: {prospect['name']}")
                    
                    # Add additional details for research-based prospects
                    prospect["description"] = f"{prospect['name']} is a potential buyer identified through AI-powered research. They operate in the {prospect['segment']} segment and are located in {prospect['location']}."
                    prospect["tradingHistory"] = []
                    prospect["complianceStatus"] = {
                        "rating": "Unknown",
                        "certifications": [],
                        "lastAudit": "N/A",
                        "issues": []
                    }
                    prospect["marketPresence"] = [prospect["location"]]
                    prospect["competitors"] = []
                    
                    return prospect
            
            logger.warning(f"Research-based prospect not found: {prospect_id}")
        except Exception as e:
            logger.error(f"Error getting research-based prospect: {str(e)}")
    
    # Check if we have detailed information for this prospect
    if prospect_id in MOCK_PROSPECT_DETAILS:
        logger.info(f"Found prospect in MOCK_PROSPECT_DETAILS: {prospect_id}")
        return MOCK_PROSPECT_DETAILS[prospect_id]
    
    # If not, find the prospect in the basic list
    for prospect in MOCK_PROSPECTS:
        if prospect["id"] == prospect_id:
            # Return basic information
            logger.info(f"Found prospect in MOCK_PROSPECTS: {prospect_id}")
            return prospect
    
    # If prospect not found, return empty dict
    logger.warning(f"Prospect not found: {prospect_id}")
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
    
    # For research-based prospects, we could use the Perplexity API to generate guidance
    if prospect.get("source") == "perplexity_research":
        # In a real implementation, we would use the Perplexity API
        # For now, return a modified version of the mock guidance
        guidance = dict(MOCK_GUIDANCE)
        guidance["talkingPoints"] = [
            f"Based on our research, {prospect['name']} could benefit from our products",
            f"They operate in the {prospect['segment']} segment, which aligns with our offerings",
            "Our research indicates they may be looking for new suppliers",
            f"They are located in {prospect['location']}, where we have distribution capabilities"
        ]
        
        # Add decision makers based on key contacts
        guidance["decisionMakers"] = []
        for contact in prospect.get("keyContacts", []):
            if "," in contact:
                name, title = contact.split(",", 1)
                guidance["decisionMakers"].append({
                    "name": name.strip(),
                    "title": title.strip(),
                    "influence": "Key decision maker",
                    "interests": "Unknown"
                })
        
        return guidance
    
    # For now, return mock guidance
    return MOCK_GUIDANCE
