"""
API tests for PharmaSage backend.

This module contains tests for the API endpoints of the PharmaSage backend using FastAPI's TestClient.
"""
import unittest
import sys
import os
from fastapi.testclient import TestClient

# Add the parent directory to the path so we can import the app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app


class TestAPI(unittest.TestCase):
    """Tests for the API endpoints."""
    
    def setUp(self):
        """Set up the test client."""
        self.client = TestClient(app)
    
    def test_dashboard_trends(self):
        """Test the dashboard trends endpoint."""
        response = self.client.get("/api/dashboard/trends")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn("global_trade_volume", data)
        self.assertIn("active_products", data)
        self.assertIn("export_companies", data)
        self.assertIn("active_markets", data)
    
    def test_search_products(self):
        """Test the search products endpoint."""
        response = self.client.get("/api/search/products?query=paracetamol")
        self.assertEqual(response.status_code, 200)
        
        products = response.json()
        self.assertIsInstance(products, list)
        if products:  # If mock data is returned
            self.assertIn("id", products[0])
            self.assertIn("api_name", products[0])
            self.assertIn("form", products[0])
    
    def test_match_prospects(self):
        """Test the match prospects endpoint."""
        response = self.client.post(
            "/api/match/prospects",
            json={
                "company_name": "Test Pharma",
                "products": ["Paracetamol", "Ibuprofen"],
                "licensed_markets": ["Europe", "North America"]
            }
        )
        self.assertEqual(response.status_code, 200)
        
        prospects = response.json()
        self.assertIsInstance(prospects, list)
        if prospects:  # If mock data is returned
            self.assertIn("id", prospects[0])
            self.assertIn("name", prospects[0])
            self.assertIn("location", prospects[0])
            self.assertIn("opportunityScore", prospects[0])
    
    def test_get_prospect_contacts(self):
        """Test the get prospect contacts endpoint."""
        # Test with a valid prospect ID
        response = self.client.get("/api/prospect/1/contacts")
        self.assertEqual(response.status_code, 200)
        
        contacts = response.json()
        self.assertIsInstance(contacts, list)
        if contacts:  # If mock data is returned
            self.assertIn("id", contacts[0])
            self.assertIn("name", contacts[0])
    
    def test_get_prospect_details(self):
        """Test the get prospect details endpoint."""
        # Test with a valid prospect ID
        response = self.client.get("/api/match/prospect/1")
        self.assertEqual(response.status_code, 200)
        
        prospect = response.json()
        self.assertIsInstance(prospect, dict)
        self.assertIn("id", prospect)
        self.assertIn("name", prospect)
        self.assertIn("location", prospect)
    
    def test_generate_outreach_guidance(self):
        """Test the generate outreach guidance endpoint."""
        # Test with a valid prospect ID
        response = self.client.post(
            "/api/match/guidance",
            json={
                "prospect_id": "1",
                "company_id": "test",
                "products": ["Paracetamol", "Ibuprofen"]
            }
        )
        self.assertEqual(response.status_code, 200)
        
        guidance = response.json()
        self.assertIsInstance(guidance, dict)
        self.assertIn("talkingPoints", guidance)
        self.assertIn("decisionMakers", guidance)
        self.assertIn("outreachStrategy", guidance)
    
    def test_search_contacts(self):
        """Test the search contacts endpoint."""
        response = self.client.post(
            "/api/prospect/contacts/search",
            json={
                "query": "Sarah",
                "company_id": None,
                "department": None,
                "seniority": None,
                "relationship_score": None
            }
        )
        self.assertEqual(response.status_code, 200)
        
        contacts = response.json()
        self.assertIsInstance(contacts, list)
        if contacts:  # If mock data is returned
            self.assertIn("id", contacts[0])
            self.assertIn("name", contacts[0])
            self.assertIn("role", contacts[0])
    
    def test_get_contact_stats(self):
        """Test the get contact stats endpoint."""
        response = self.client.get("/api/prospect/stats")
        self.assertEqual(response.status_code, 200)
        
        stats = response.json()
        self.assertIsInstance(stats, dict)
        self.assertIn("total_contacts", stats)
        self.assertIn("key_contacts", stats)
        self.assertIn("recent_interactions", stats)
        self.assertIn("companies", stats)


if __name__ == "__main__":
    unittest.main()
