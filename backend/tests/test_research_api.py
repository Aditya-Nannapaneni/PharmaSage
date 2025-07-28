"""
Tests for the Research API endpoints.

This module contains tests for the Research API endpoints.
"""
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from app.main import app
from app.core.config import settings


client = TestClient(app)


def test_research_status_endpoint():
    """Test the research status endpoint."""
    response = client.get("/api/research/status")
    
    assert response.status_code == 200
    data = response.json()
    
    # Check that the response contains the expected fields
    assert "service" in data
    assert "status" in data
    assert "mode" in data
    assert "api_configured" in data
    assert "message" in data
    
    # Check that the mode matches the settings
    assert data["mode"] == "mock" if settings.USE_MOCK_RESPONSES else "live"


@patch("app.services.buyer_research.research_potential_buyers")
def test_research_buyers_endpoint(mock_research):
    """Test the research buyers endpoint."""
    # Mock the research function
    mock_buyers = [
        {
            "id": "research-1",
            "name": "Test Company",
            "location": "USA",
            "segment": "Pharmaceuticals",
            "website": "https://example.com",
            "keyContacts": ["John Doe, CEO"],
            "reasonForRecommendation": "Good fit for your products",
            "opportunityScore": 85,
            "status": "High Priority",
            "source": "perplexity_research"
        }
    ]
    mock_research.return_value = mock_buyers
    
    # Make the request
    response = client.post(
        "/api/research/buyers",
        json={
            "company_name": "Source Company",
            "company_website": "https://sourcecompany.com",
            "products": ["Product A", "Product B"]
        }
    )
    
    # Check the response
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Test Company"
    assert data[0]["website"] == "https://example.com"
    
    # Verify that the research function was called with the correct arguments
    mock_research.assert_called_once()
    args, kwargs = mock_research.call_args
    assert args[1] == "Source Company"
    assert args[2] == "https://sourcecompany.com"
    assert args[3] == ["Product A", "Product B"]


@patch("app.services.buyer_research.research_potential_buyers")
def test_research_buyers_endpoint_error(mock_research):
    """Test the research buyers endpoint when an error occurs."""
    # Mock the research function to raise an exception
    mock_research.side_effect = Exception("Research failed")
    
    # Make the request
    response = client.post(
        "/api/research/buyers",
        json={
            "company_name": "Source Company",
            "company_website": "https://sourcecompany.com",
            "products": ["Product A", "Product B"]
        }
    )
    
    # Check the response
    assert response.status_code == 500
    data = response.json()
    assert "detail" in data
    assert "Research failed" in data["detail"]


def test_research_buyers_endpoint_validation():
    """Test the research buyers endpoint with invalid input."""
    # Missing required fields
    response = client.post(
        "/api/research/buyers",
        json={
            "company_name": "Source Company"
            # Missing company_website and products
        }
    )
    
    # Check the response
    assert response.status_code == 422  # Unprocessable Entity
