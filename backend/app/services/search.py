"""
Search service.

This module provides services for searching products and companies.
"""
from typing import Dict, List, Any, Optional
from sqlalchemy.orm import Session

# Mock data for development
MOCK_PRODUCTS = [
    {"id": "1", "api_name": "Paracetamol", "synonyms": ["Acetaminophen"], "code": "N02BE01", "form": "API", "therapeutic_category": "Analgesic"},
    {"id": "2", "api_name": "Ibuprofen", "synonyms": ["Advil", "Motrin"], "code": "M01AE01", "form": "API", "therapeutic_category": "NSAID"},
    {"id": "3", "api_name": "Amoxicillin", "synonyms": ["Amoxil"], "code": "J01CA04", "form": "API", "therapeutic_category": "Antibiotic"},
    {"id": "4", "api_name": "Omeprazole", "synonyms": ["Prilosec"], "code": "A02BC01", "form": "API", "therapeutic_category": "PPI"},
    {"id": "5", "api_name": "Metformin", "synonyms": ["Glucophage"], "code": "A10BA02", "form": "API", "therapeutic_category": "Antidiabetic"},
    {"id": "6", "api_name": "Atorvastatin", "synonyms": ["Lipitor"], "code": "C10AA05", "form": "API", "therapeutic_category": "Statin"},
    {"id": "7", "api_name": "Losartan", "synonyms": ["Cozaar"], "code": "C09CA01", "form": "API", "therapeutic_category": "ARB"},
    {"id": "8", "api_name": "Amlodipine", "synonyms": ["Norvasc"], "code": "C08CA01", "form": "API", "therapeutic_category": "CCB"},
    {"id": "9", "api_name": "Sertraline", "synonyms": ["Zoloft"], "code": "N06AB06", "form": "API", "therapeutic_category": "SSRI"},
    {"id": "10", "api_name": "Fluoxetine", "synonyms": ["Prozac"], "code": "N06AB03", "form": "API", "therapeutic_category": "SSRI"}
]

MOCK_COMPANIES = [
    {"id": "1", "name": "Teva Pharmaceutical", "country": "Israel", "sector": "Generic Medications", "size": "Large"},
    {"id": "2", "name": "Novartis", "country": "Switzerland", "sector": "Specialty Drugs", "size": "Large"},
    {"id": "3", "name": "Pfizer", "country": "United States", "sector": "Vaccines", "size": "Large"},
    {"id": "4", "name": "Roche", "country": "Switzerland", "sector": "Diagnostics", "size": "Large"},
    {"id": "5", "name": "Johnson & Johnson", "country": "United States", "sector": "Consumer Health", "size": "Large"},
    {"id": "6", "name": "MedCore Pharmaceuticals", "country": "Germany", "sector": "Generic Medications", "size": "Medium"},
    {"id": "7", "name": "BioPharma Solutions", "country": "Brazil", "sector": "Specialty Drugs", "size": "Medium"},
    {"id": "8", "name": "Global Health Networks", "country": "India", "sector": "Distribution", "size": "Medium"},
    {"id": "9", "name": "PharmaVision Corp", "country": "Canada", "sector": "Research & Development", "size": "Small"},
    {"id": "10", "name": "MediTech Innovations", "country": "Japan", "sector": "Medical Devices", "size": "Small"}
]

MOCK_REGIONS = [
    "North America",
    "Europe",
    "Asia Pacific",
    "Latin America",
    "Africa",
    "Middle East"
]


def search_products(
    db: Session, 
    query: str, 
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Search for pharmaceutical products.
    
    Args:
        db: Database session
        query: Search query string
        limit: Maximum number of results to return
        
    Returns:
        List of matching products
    """
    # In a real implementation, this would query the database
    # For now, return mock data filtered by the query
    
    query = query.lower()
    results = []
    
    for product in MOCK_PRODUCTS:
        # Check if query matches product name or code
        if query in product["api_name"].lower() or query in product["code"].lower():
            results.append(product)
            continue
            
        # Check if query matches any synonym
        if any(query in synonym.lower() for synonym in product["synonyms"]):
            results.append(product)
            continue
    
    # Limit the results
    return results[:limit]


def search_companies(
    db: Session, 
    query: str, 
    country: Optional[str] = None, 
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Search for pharmaceutical companies.
    
    Args:
        db: Database session
        query: Search query string
        country: Optional country filter
        limit: Maximum number of results to return
        
    Returns:
        List of matching companies
    """
    # In a real implementation, this would query the database
    # For now, return mock data filtered by the query and country
    
    query = query.lower()
    results = []
    
    for company in MOCK_COMPANIES:
        # Apply country filter if specified
        if country and company["country"].lower() != country.lower():
            continue
            
        # Check if query matches company name or sector
        if query in company["name"].lower() or query in company["sector"].lower():
            results.append(company)
    
    # Limit the results
    return results[:limit]


def get_regions(db: Session) -> List[str]:
    """
    Get available regions.
    
    Args:
        db: Database session
        
    Returns:
        List of region names
    """
    # In a real implementation, this would query the database
    # For now, return mock data
    return MOCK_REGIONS
