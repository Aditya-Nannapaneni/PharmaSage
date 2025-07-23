"""
Export API endpoints.

This module provides API endpoints for exporting data from the system.
"""
from typing import Dict, List, Any, Optional
from fastapi import APIRouter, Depends, Body, Query, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services import export as export_service

router = APIRouter()


@router.post("/results", response_model=Dict[str, str])
async def export_search_results(
    result_ids: List[str] = Body(..., description="List of result IDs to export"),
    export_type: str = Query("csv", description="Export format (csv, xlsx)"),
    include_contacts: bool = Query(True, description="Include contact information"),
    db: Session = Depends(get_db),
) -> Dict[str, str]:
    """
    Export search or match results.
    
    This endpoint exports search or match results to a downloadable file.
    
    Args:
        result_ids: List of result IDs to export
        export_type: Export format (csv, xlsx)
        include_contacts: Whether to include contact information
        db: Database session
        
    Returns:
        Dictionary with download URL
    """
    try:
        return export_service.export_results(db, result_ids, export_type, include_contacts)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/download/{file_id}", response_class=FileResponse)
async def download_export(
    file_id: str,
    db: Session = Depends(get_db),
) -> FileResponse:
    """
    Download an exported file.
    
    This endpoint downloads a previously exported file.
    
    Args:
        file_id: ID of the exported file
        db: Database session
        
    Returns:
        File download response
    """
    try:
        file_path, file_name = export_service.get_export_file(db, file_id)
        return FileResponse(
            path=file_path,
            filename=file_name,
            media_type="application/octet-stream",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/dashboard", response_model=Dict[str, str])
async def export_dashboard_data(
    dashboard_type: str = Body(..., description="Type of dashboard data to export"),
    filters: Dict[str, Any] = Body({}, description="Filters to apply to the data"),
    export_type: str = Query("csv", description="Export format (csv, xlsx)"),
    db: Session = Depends(get_db),
) -> Dict[str, str]:
    """
    Export dashboard data.
    
    This endpoint exports dashboard data to a downloadable file.
    
    Args:
        dashboard_type: Type of dashboard data to export
        filters: Filters to apply to the data
        export_type: Export format (csv, xlsx)
        db: Database session
        
    Returns:
        Dictionary with download URL
    """
    try:
        return export_service.export_dashboard_data(db, dashboard_type, filters, export_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
