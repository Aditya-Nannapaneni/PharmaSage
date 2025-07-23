"""
Unit tests for PharmaSage backend services.

This module contains unit tests for the service layer of the PharmaSage backend.
"""
import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add the parent directory to the path so we can import the app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services import dashboard, search, matching, contacts


class TestDashboardService(unittest.TestCase):
    """Tests for the dashboard service."""
    
    def test_get_market_trends(self):
        """Test getting market trends."""
        # Create a mock database session
        mock_db = MagicMock()
        
        # Call the service function
        result = dashboard.get_market_trends(mock_db)
        
        # Assert the result structure
        self.assertIsInstance(result, dict)
        self.assertIn('global_trade_volume', result)
        self.assertIn('active_products', result)
        self.assertIn('export_companies', result)
        self.assertIn('active_markets', result)
        
        # Check the values
        self.assertIsInstance(result['global_trade_volume'], dict)
        self.assertIn('value', result['global_trade_volume'])
        self.assertIn('unit', result['global_trade_volume'])
        self.assertIn('trend', result['global_trade_volume'])


class TestSearchService(unittest.TestCase):
    """Tests for the search service."""
    
    def test_search_products(self):
        """Test searching for products."""
        # Create a mock database session
        mock_db = MagicMock()
        
        # Call the service function
        result = search.search_products(mock_db, "paracetamol")
        
        # Assert the result structure
        self.assertIsInstance(result, list)
        if result:  # If mock data is returned
            self.assertIsInstance(result[0], dict)
            self.assertIn('id', result[0])
            self.assertIn('api_name', result[0])
            self.assertIn('form', result[0])


class TestMatchingService(unittest.TestCase):
    """Tests for the matching service."""
    
    def test_find_prospects(self):
        """Test finding prospects."""
        # Create a mock database session
        mock_db = MagicMock()
        
        # Call the service function
        result = matching.find_prospects(
            mock_db, 
            "Test Pharma", 
            ["Paracetamol", "Ibuprofen"], 
            ["Europe", "North America"]
        )
        
        # Assert the result structure
        self.assertIsInstance(result, list)
        if result:  # If mock data is returned
            self.assertIsInstance(result[0], dict)
            self.assertIn('id', result[0])
            self.assertIn('name', result[0])
            self.assertIn('location', result[0])
            self.assertIn('opportunityScore', result[0])


class TestContactsService(unittest.TestCase):
    """Tests for the contacts service."""
    
    def test_get_prospect_contacts(self):
        """Test getting contacts for a prospect."""
        # Create a mock database session
        mock_db = MagicMock()
        
        # Call the service function with a prospect ID
        result = contacts.get_prospect_contacts(mock_db, "1")
        
        # Assert the result structure
        self.assertIsInstance(result, list)
        if result:  # If mock data is returned
            self.assertIsInstance(result[0], dict)
            self.assertIn('id', result[0])
            self.assertIn('name', result[0])
            self.assertIn('role', result[0])
    
    def test_search_contacts(self):
        """Test searching for contacts."""
        # Create a mock database session
        mock_db = MagicMock()
        
        # Call the service function
        result = contacts.search_contacts(mock_db, query="Sarah")
        
        # Assert the result structure
        self.assertIsInstance(result, list)
        if result:  # If mock data is returned
            self.assertIsInstance(result[0], dict)
            self.assertIn('id', result[0])
            self.assertIn('name', result[0])
            self.assertIn('role', result[0])
    
    def test_get_contact_stats(self):
        """Test getting contact statistics."""
        # Create a mock database session
        mock_db = MagicMock()
        
        # Call the service function
        result = contacts.get_contact_stats(mock_db)
        
        # Assert the result structure
        self.assertIsInstance(result, dict)
        self.assertIn('total_contacts', result)
        self.assertIn('key_contacts', result)
        self.assertIn('recent_interactions', result)
        self.assertIn('companies', result)


if __name__ == "__main__":
    unittest.main()
