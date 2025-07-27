"""
Tests for the buyer research service.
"""
import unittest
from unittest.mock import patch, MagicMock
from sqlalchemy.orm import Session

from app.services.buyer_research import (
    format_prompt_with_company_data,
    extract_section_from_markdown,
    parse_markdown_table,
    parse_research_results,
    research_potential_buyers
)


class TestBuyerResearch(unittest.TestCase):
    """Test cases for the buyer research service."""

    def test_format_prompt_with_company_data(self):
        """Test the format_prompt_with_company_data function."""
        # Mock the prompt template
        with patch('app.services.buyer_research.PROSPECT_IDENTIFICATION_PROMPT', 
                  'Test prompt with <source_company_url>'):
            # Call the function
            result = format_prompt_with_company_data('https://example.com')
            
            # Check that the function returned the expected result
            self.assertEqual(result, 'Test prompt with https://example.com')

    def test_extract_section_from_markdown(self):
        """Test the extract_section_from_markdown function."""
        # Test markdown with multiple sections
        markdown = """
        # Section 1
        Content for section 1

        # Section 2
        Content for section 2

        ## Subsection 2.1
        Subsection content

        # Section 3
        Content for section 3
        """
        # Extract section 2
        result = extract_section_from_markdown(markdown, "Section 2")
        self.assertEqual(result, "Content for section 2")
        
        # Extract section that doesn't exist
        result = extract_section_from_markdown(markdown, "Section 4")
        self.assertIsNone(result)

    def test_parse_markdown_table(self):
        """Test the parse_markdown_table function."""
        # Test markdown table
        table = """
| Name | Age | Location |
| ---- | --- | -------- |
| John | 30  | New York |
| Jane | 25  | London   |
| Bob  | 35  | Tokyo    |
"""
        # Parse the table
        result = parse_markdown_table(table)
        
        # Check that the function returned the expected result
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], {"Name": "John", "Age": "30", "Location": "New York"})
        self.assertEqual(result[1], {"Name": "Jane", "Age": "25", "Location": "London"})
        self.assertEqual(result[2], {"Name": "Bob", "Age": "35", "Location": "Tokyo"})
        
        # Test empty table
        result = parse_markdown_table("")
        self.assertEqual(result, [])
        
        # Test table with only headers
        result = parse_markdown_table("| Name | Age |\n| ---- | --- |")
        self.assertEqual(result, [])

    def test_parse_research_results(self):
        """Test the parse_research_results function."""
        # Mock research response
        research_response = {
            "text": """
# Source Company Overview
Test company overview

# Recommended Target Companies Table
| Company Name | Website | Country/Region | Target Segment | Key Contacts | Reason for Recommendation |
| ------------ | ------- | -------------- | ------------- | ------------ | ------------------------- |
| Company A | https://a.com | USA | Pharma | John Doe, CEO | Good fit for products |
| Company B | https://b.com | UK | Biotech | Jane Smith, CTO | Expanding in this area |
"""
        }
        
        # Parse the research results
        result = parse_research_results(research_response)
        
        # Check that the function returned the expected result
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["name"], "Company A")
        self.assertEqual(result[0]["website"], "https://a.com")
        self.assertEqual(result[0]["location"], "USA")
        self.assertEqual(result[0]["segment"], "Pharma")
        self.assertEqual(result[0]["keyContacts"], ["John Doe, CEO"])
        self.assertEqual(result[0]["reasonForRecommendation"], "Good fit for products")
        self.assertEqual(result[0]["source"], "perplexity_research")
        
        # Test with missing table section
        research_response = {"text": "# Source Company Overview\nTest company overview"}
        result = parse_research_results(research_response)
        self.assertEqual(result, [])
        
        # Test with invalid response format
        research_response = {"invalid": "format"}
        result = parse_research_results(research_response)
        self.assertEqual(result, [])

    @patch('app.services.buyer_research.run_deep_research_with_cache')
    @patch('app.services.buyer_research.format_prompt_with_company_data')
    def test_research_potential_buyers(self, mock_format_prompt, mock_run_deep_research):
        """Test the research_potential_buyers function."""
        # Mock the dependencies
        mock_format_prompt.return_value = "Formatted prompt"
        mock_run_deep_research.return_value = {
            "text": """
# Recommended Target Companies Table
| Company Name | Website | Country/Region | Target Segment | Key Contacts | Reason for Recommendation |
| ------------ | ------- | -------------- | ------------- | ------------ | ------------------------- |
| Company A | https://a.com | USA | Pharma | John Doe, CEO | Good fit for products |
"""
        }
        
        # Call the function
        result = research_potential_buyers(
            db=MagicMock(spec=Session),
            company_name="Test Company",
            company_website="https://example.com",
            products=["Product A", "Product B"]
        )
        
        # Check that the function called the dependencies with the correct parameters
        mock_format_prompt.assert_called_once_with("https://example.com")
        mock_run_deep_research.assert_called_once_with("Formatted prompt")
        
        # Check that the function returned the expected result
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Company A")
        self.assertEqual(result[0]["source"], "perplexity_research")


if __name__ == '__main__':
    unittest.main()
