"""
Tests for the Perplexity API client.
"""
import os
import unittest
from unittest.mock import patch, MagicMock
import json
from datetime import datetime, timedelta

from app.services.perplexity_client import run_deep_research, run_deep_research_with_cache


class TestPerplexityClient(unittest.TestCase):
    """Test cases for the Perplexity API client."""

    @patch('app.services.perplexity_client.requests.post')
    @patch('app.services.perplexity_client.PERPLEXITY_API_KEY', 'test_api_key')
    @patch('app.services.perplexity_client.USE_MOCK_RESPONSES', False)
    def test_run_deep_research(self, mock_post):
        """Test the run_deep_research function."""
        # Mock the response from the Perplexity API
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "This is a test response from the Perplexity API."}}]
        }
        mock_post.return_value = mock_response

        # Call the function
        result = run_deep_research("Test prompt")

        # Check that the function called the API with the correct parameters
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        self.assertEqual(kwargs['json']['messages'][0]['content'], "Test prompt")
        self.assertEqual(kwargs['json']['model'], "sonar-medium-online")
        self.assertEqual(kwargs['headers']['Authorization'], "Bearer test_api_key")

        # Check that the function returned the expected result
        self.assertEqual(result, {"text": "This is a test response from the Perplexity API."})

    @patch('app.services.perplexity_client.run_deep_research')
    def test_run_deep_research_with_cache(self, mock_run_deep_research):
        """Test the run_deep_research_with_cache function."""
        # Mock the response from run_deep_research
        mock_run_deep_research.return_value = {
            "text": "This is a test response from the Perplexity API."
        }

        # Call the function twice with the same prompt
        result1 = run_deep_research_with_cache("Test prompt")
        result2 = run_deep_research_with_cache("Test prompt")

        # Check that run_deep_research was called only once
        mock_run_deep_research.assert_called_once()

        # Check that both calls returned the same result
        self.assertEqual(result1, result2)

    @patch('app.services.perplexity_client.PERPLEXITY_API_KEY', None)
    @patch('app.services.perplexity_client.USE_MOCK_RESPONSES', False)
    def test_run_deep_research_no_api_key(self):
        """Test that run_deep_research raises an exception when no API key is provided."""
        with self.assertRaises(Exception) as context:
            run_deep_research("Test prompt")
        
        self.assertIn("API key not configured", str(context.exception))

    @patch('app.services.perplexity_client.requests.post')
    @patch('app.services.perplexity_client.PERPLEXITY_API_KEY', 'test_api_key')
    @patch('app.services.perplexity_client.USE_MOCK_RESPONSES', False)
    def test_run_deep_research_with_max_tokens(self, mock_post):
        """Test the run_deep_research function with max_tokens parameter."""
        # Mock the response from the Perplexity API
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "This is a test response from the Perplexity API."}}]
        }
        mock_post.return_value = mock_response

        # Call the function with max_tokens
        result = run_deep_research("Test prompt", max_tokens=100)

        # Check that the function called the API with the correct parameters
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        self.assertEqual(kwargs['json']['messages'][0]['content'], "Test prompt")
        self.assertEqual(kwargs['json']['max_tokens'], 100)
        self.assertEqual(kwargs['headers']['Authorization'], "Bearer test_api_key")

        # Check that the function returned the expected result
        self.assertEqual(result, {"text": "This is a test response from the Perplexity API."})

    @patch('app.services.perplexity_client.USE_MOCK_RESPONSES', True)
    def test_run_deep_research_with_mock(self):
        """Test the run_deep_research function with mock responses."""
        # Call the function
        result = run_deep_research("Test prompt with https://example.com")

        # Check that the function returned a mock response
        self.assertIn("text", result)
        self.assertIn("Example is a pharmaceutical company", result["text"])


if __name__ == '__main__':
    unittest.main()
