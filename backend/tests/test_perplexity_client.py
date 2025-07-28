"""
Tests for the Perplexity API client.

This module contains tests for the Perplexity API client functionality.
"""
import pytest
from unittest.mock import patch, MagicMock

from app.services.perplexity_client import (
    run_deep_research,
    run_deep_research_with_cache,
    USE_MOCK_RESPONSES,
    _get_mock_response
)
from app.core.config import settings


def test_use_mock_responses_from_settings():
    """Test that USE_MOCK_RESPONSES is set from settings."""
    assert USE_MOCK_RESPONSES == settings.USE_MOCK_RESPONSES


def test_mock_response_generation():
    """Test that the mock response generator works correctly."""
    # Test with a URL in the prompt
    prompt_with_url = "Analyze the company at https://example.com and find potential buyers"
    mock_response = _get_mock_response(prompt_with_url)
    
    # Verify the response structure
    assert "text" in mock_response
    assert "Source Company Overview" in mock_response["text"]
    assert "Example" in mock_response["text"]  # Company name extracted from URL
    assert "Recommended Target Companies Table" in mock_response["text"]
    
    # Test with a different URL
    prompt_with_different_url = "Analyze the company at https://pharma.com and find potential buyers"
    mock_response = _get_mock_response(prompt_with_different_url)
    assert "Pharma" in mock_response["text"]


@patch("app.services.perplexity_client.USE_MOCK_RESPONSES", True)
def test_run_deep_research_with_mock():
    """Test that run_deep_research uses mock data when USE_MOCK_RESPONSES is True."""
    with patch("app.services.perplexity_client._get_mock_response") as mock_get_response:
        mock_get_response.return_value = {"text": "Mock response"}
        
        result = run_deep_research("Test prompt")
        
        # Verify that _get_mock_response was called
        mock_get_response.assert_called_once_with("Test prompt")
        assert result == {"text": "Mock response"}


@patch("app.services.perplexity_client.USE_MOCK_RESPONSES", False)
@patch("app.services.perplexity_client.PERPLEXITY_API_KEY", "fake-api-key")
@patch("requests.post")
def test_run_deep_research_with_real_api(mock_post):
    """Test that run_deep_research calls the API when USE_MOCK_RESPONSES is False."""
    # Mock the API response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "choices": [
            {
                "message": {
                    "content": "API response content"
                }
            }
        ]
    }
    mock_response.raise_for_status = MagicMock()
    mock_post.return_value = mock_response
    
    result = run_deep_research("Test prompt")
    
    # Verify that requests.post was called with the correct arguments
    mock_post.assert_called_once()
    args, kwargs = mock_post.call_args
    assert "https://api.perplexity.ai/chat/completions" in args
    assert kwargs["json"]["messages"][0]["content"] == "Test prompt"
    assert kwargs["headers"]["Authorization"] == "Bearer fake-api-key"
    
    # Verify the result
    assert result == {"text": "API response content"}


@patch("app.services.perplexity_client.run_deep_research")
def test_run_deep_research_with_cache(mock_run_deep_research):
    """Test that the cache works correctly."""
    mock_run_deep_research.return_value = {"text": "Research result"}
    
    # First call should miss the cache
    result1 = run_deep_research_with_cache("Test prompt")
    mock_run_deep_research.assert_called_once_with("Test prompt", None)
    assert result1 == {"text": "Research result"}
    
    # Reset the mock
    mock_run_deep_research.reset_mock()
    
    # Second call with the same prompt should hit the cache
    result2 = run_deep_research_with_cache("Test prompt")
    mock_run_deep_research.assert_not_called()
    assert result2 == {"text": "Research result"}
    
    # Call with a different prompt should miss the cache
    result3 = run_deep_research_with_cache("Different prompt")
    mock_run_deep_research.assert_called_once_with("Different prompt", None)
