"""
Contacts service.

This module provides services for the contact intelligence functionality.
"""
from typing import Dict, List, Any, Optional
from sqlalchemy.orm import Session

# Mock data for development
MOCK_CONTACTS = [
    {
        "id": "1",
        "name": "Dr. Sarah Chen",
        "role": "Chief Procurement Officer",
        "company_id": "1",
        "company_name": "MedCore Pharmaceuticals",
        "linkedin_url": "https://linkedin.com/in/sarahchen",
        "email": "s.chen@medcore.com",
        "phone": "+49 30 1234567",
        "department": "Procurement",
        "seniority": "C-Level",
        "relationship_score": 95,
        "interactions": 23,
        "last_interaction": "2 days ago",
        "notes": "Key decision maker for European procurement. Very responsive to innovative solutions."
    },
    {
        "id": "2",
        "name": "Thomas Weber",
        "role": "Head of R&D",
        "company_id": "1",
        "company_name": "MedCore Pharmaceuticals",
        "linkedin_url": "https://linkedin.com/in/thomasweber",
        "email": "t.weber@medcore.com",
        "phone": "+49 30 1234568",
        "department": "Research & Development",
        "seniority": "Director Level",
        "relationship_score": 82,
        "interactions": 15,
        "last_interaction": "1 week ago",
        "notes": "Technical evaluator for new suppliers. Focused on quality and consistency."
    },
    {
        "id": "3",
        "name": "Marcus Rodriguez",
        "role": "VP of Business Development",
        "company_id": "2",
        "company_name": "BioPharma Solutions",
        "linkedin_url": "https://linkedin.com/in/marcusrodriguez",
        "email": "m.rodriguez@biopharma.com",
        "phone": "+55 11 9876543",
        "department": "Business Development",
        "seniority": "VP Level",
        "relationship_score": 82,
        "interactions": 18,
        "last_interaction": "5 days ago",
        "notes": "Excellent contact for Latin American expansion. Focus on strategic partnerships."
    },
    {
        "id": "4",
        "name": "Dr. Priya Sharma",
        "role": "Head of Research",
        "company_id": "3",
        "company_name": "Global Health Networks",
        "linkedin_url": "https://linkedin.com/in/priyasharma",
        "email": "p.sharma@globalhealth.in",
        "phone": "+91 22 5555123",
        "department": "Research & Development",
        "seniority": "Director Level",
        "relationship_score": 78,
        "interactions": 15,
        "last_interaction": "1 week ago",
        "notes": "Leading expert in drug distribution networks. Values evidence-based approaches."
    },
    {
        "id": "5",
        "name": "James Mitchell",
        "role": "Senior Director of Operations",
        "company_id": "4",
        "company_name": "PharmaVision Corp",
        "linkedin_url": "https://linkedin.com/in/jamesmitchell",
        "email": "j.mitchell@pharmavision.ca",
        "phone": "+1 416 7778888",
        "department": "Operations",
        "seniority": "Senior Director",
        "relationship_score": 88,
        "interactions": 31,
        "last_interaction": "3 days ago",
        "notes": "Operations expert with focus on efficiency and cost optimization."
    }
]

MOCK_CONTACT_STATS = {
    "total_contacts": 8942,
    "key_contacts": 234,
    "recent_interactions": 1847,
    "companies": 1203,
    "department_breakdown": [
        {"department": "Procurement", "count": 2156},
        {"department": "R&D", "count": 1872},
        {"department": "Business Development", "count": 1543},
        {"department": "Operations", "count": 1289},
        {"department": "Executive", "count": 982},
        {"department": "Other", "count": 1100}
    ],
    "seniority_breakdown": [
        {"level": "C-Level", "count": 423},
        {"level": "VP Level", "count": 876},
        {"level": "Director Level", "count": 2134},
        {"level": "Manager Level", "count": 3245},
        {"level": "Other", "count": 2264}
    ]
}


def get_prospect_contacts(
    db: Session, 
    prospect_id: str
) -> List[Dict[str, Any]]:
    """
    Get contacts for a prospect.
    
    Args:
        db: Database session
        prospect_id: ID of the prospect
        
    Returns:
        List of contacts for the prospect
    """
    # In a real implementation, this would query the database
    # For now, return mock data filtered by company_id
    
    return [contact for contact in MOCK_CONTACTS if contact["company_id"] == prospect_id]


def search_contacts(
    db: Session, 
    query: Optional[str] = None, 
    company_id: Optional[str] = None, 
    department: Optional[str] = None, 
    seniority: Optional[str] = None, 
    relationship_score: Optional[str] = None, 
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Search for contacts.
    
    Args:
        db: Database session
        query: Search query for contact name or title
        company_id: Filter by company ID
        department: Filter by department
        seniority: Filter by seniority level
        relationship_score: Filter by relationship score
        limit: Maximum number of contacts to return
        
    Returns:
        List of matching contacts
    """
    # In a real implementation, this would query the database
    # For now, return mock data filtered by the parameters
    
    results = []
    
    for contact in MOCK_CONTACTS:
        # Apply company filter if specified
        if company_id and contact["company_id"] != company_id:
            continue
            
        # Apply department filter if specified
        if department and contact["department"] != department:
            continue
            
        # Apply seniority filter if specified
        if seniority and contact["seniority"] != seniority:
            continue
            
        # Apply relationship score filter if specified
        if relationship_score:
            # Parse relationship score filter (e.g., "80-100")
            try:
                min_score, max_score = map(int, relationship_score.split("-"))
                if not (min_score <= contact["relationship_score"] <= max_score):
                    continue
            except ValueError:
                # If parsing fails, ignore this filter
                pass
                
        # Apply query filter if specified
        if query:
            query = query.lower()
            if query not in contact["name"].lower() and query not in contact["role"].lower():
                continue
                
        # If all filters pass, add contact to results
        results.append(contact)
    
    # Limit the results
    return results[:limit]


def get_contact_stats(db: Session) -> Dict[str, Any]:
    """
    Get contact statistics.
    
    Args:
        db: Database session
        
    Returns:
        Contact statistics
    """
    # In a real implementation, this would query the database
    # For now, return mock data
    return MOCK_CONTACT_STATS
