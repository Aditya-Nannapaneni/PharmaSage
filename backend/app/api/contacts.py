"""
Contacts API endpoints.

This module provides API endpoints for the contact intelligence functionality.
"""
from typing import Dict, List, Any, Optional
from fastapi import APIRouter, Depends, Path, Query, Body, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services import contacts as contacts_service

router = APIRouter()


@router.get("/{prospect_id}/contacts", response_model=List[Dict[str, Any]])
async def get_prospect_contacts(
    prospect_id: str = Path(..., description="ID of the prospect"),
    db: Session = Depends(get_db),
) -> List[Dict[str, Any]]:
    """
    Get contacts for a prospect.
    
    This endpoint retrieves contact information for a specific prospect.
    
    Args:
        prospect_id: ID of the prospect
        db: Database session
        
    Returns:
        List of contacts for the prospect
    """
    try:
        return contacts_service.get_prospect_contacts(db, prospect_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/contacts/search", response_model=List[Dict[str, Any]])
async def search_contacts(
    query: Optional[str] = Body(None, description="Search query for contact name or title"),
    company_id: Optional[str] = Body(None, description="Filter by company ID"),
    department: Optional[str] = Body(None, description="Filter by department"),
    seniority: Optional[str] = Body(None, description="Filter by seniority level"),
    relationship_score: Optional[str] = Body(None, description="Filter by relationship score"),
    limit: int = Query(10, description="Maximum number of contacts to return"),
    db: Session = Depends(get_db),
) -> List[Dict[str, Any]]:
    """
    Search for contacts.
    
    This endpoint provides search functionality for contacts based on various criteria.
    
    Args:
        query: Search query for contact name or title
        company_id: Filter by company ID
        department: Filter by department
        seniority: Filter by seniority level
        relationship_score: Filter by relationship score
        limit: Maximum number of contacts to return
        db: Database session
        
    Returns:
        List of matching contacts
    """
    try:
        return contacts_service.search_contacts(
            db, query, company_id, department, seniority, relationship_score, limit
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stats", response_model=Dict[str, Any])
async def get_contact_stats(
    db: Session = Depends(get_db),
) -> Dict[str, Any]:
    """
    Get contact statistics.
    
    This endpoint provides statistics about contacts in the system,
    such as total contacts, key contacts, recent interactions, etc.
    
    Args:
        db: Database session
        
    Returns:
        Contact statistics
    """
    try:
        return contacts_service.get_contact_stats(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
