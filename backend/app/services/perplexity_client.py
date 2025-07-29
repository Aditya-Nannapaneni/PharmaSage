"""
Perplexity API client.

This module provides a client for the Perplexity Deep Research API.
"""
import os
import logging
import requests
import hashlib
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

from app.core.config import settings

# Configure logging
logger = logging.getLogger(__name__)

# API configuration
PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"  # Updated endpoint based on documentation
PERPLEXITY_API_KEY = settings.PERPLEXITY_API_KEY

# Flag to use mock responses for testing - use the setting from config
USE_MOCK_RESPONSES = settings.USE_MOCK_RESPONSES

# Print the value of USE_MOCK_RESPONSES for debugging
print(f"USE_MOCK_RESPONSES: {USE_MOCK_RESPONSES}")
logger.info(f"USE_MOCK_RESPONSES: {USE_MOCK_RESPONSES}")

def run_deep_research(prompt: str, max_tokens: Optional[int] = None) -> Dict[str, Any]:
    """
    Execute a deep research query using the Perplexity API.
    
    Args:
        prompt: The research prompt to send to Perplexity
        max_tokens: Optional maximum number of tokens for the response
        
    Returns:
        The JSON response from the Perplexity API
        
    Raises:
        Exception: If the API request fails
    """
    if not PERPLEXITY_API_KEY and not USE_MOCK_RESPONSES:
        logger.error("Perplexity API key not found in environment variables")
        raise Exception("Perplexity API key not configured. Please set the PERPLEXITY_API_KEY environment variable.")
    
    # Use mock response for testing
    if USE_MOCK_RESPONSES:
        logger.info("Using mock response for testing")
        return _get_mock_response(prompt)
    
    try:
        headers = {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }
        
        # Updated payload with correct model name based on documentation
        payload = {
            "model": "sonar-deep-research",  # Using the correct model name from documentation
            "messages": [{"role": "user", "content": prompt}]
        }
        
        # Add max_tokens if specified
        if max_tokens:
            payload["max_tokens"] = max_tokens
        
        logger.info(f"Sending request to Perplexity API: {PERPLEXITY_API_URL}")
        logger.info(f"Request payload: {json.dumps(payload)}")
        response = requests.post(PERPLEXITY_API_URL, json=payload, headers=headers)
        
        # Log response status and headers for debugging
        logger.info(f"Response status: {response.status_code}")
        logger.info(f"Response headers: {response.headers}")
        
        if not response.ok:
            logger.error(f"Error response body: {response.text}")
            
        response.raise_for_status()
        
        # Extract the text from the response
        api_response = response.json()
        logger.info(f"API response structure: {json.dumps(api_response)[:500]}...")
        
        # Extract the content from the choices array and add it to the response as "text"
        # This ensures compatibility with the existing parsing code
        if "choices" in api_response and len(api_response["choices"]) > 0:
            message = api_response["choices"][0].get("message", {})
            content = message.get("content", "")
            api_response["text"] = content
        
        return api_response
    
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429:
            # Rate limit exceeded
            logger.warning("Perplexity API rate limit exceeded")
            raise Exception("Research service temporarily unavailable. Please try again later.")
        elif e.response.status_code == 401:
            # Authentication error
            logger.error("Perplexity API authentication failed")
            raise Exception("Research service configuration error. Please contact support.")
        else:
            logger.error(f"Perplexity API error: {str(e)}")
            # Try to get more details from the response
            error_detail = ""
            try:
                error_detail = e.response.json().get("error", {}).get("message", "")
            except:
                pass
            if error_detail:
                logger.error(f"API error details: {error_detail}")
            raise Exception(f"Research service error: {str(e)}")
    
    except Exception as e:
        logger.error(f"Unexpected error in Perplexity client: {str(e)}")
        raise Exception("An unexpected error occurred. Please try again later.")


def _get_mock_response(prompt: str) -> Dict[str, Any]:
    """
    Generate a mock response for testing purposes.
    
    Args:
        prompt: The research prompt
        
    Returns:
        A mock response
    """
    # Extract the company website from the prompt
    import re
    website_match = re.search(r'https?://[^\s>"]+', prompt)
    company_website = website_match.group(0) if website_match else "example.com"
    
    # Generate a company name from the website
    company_name = company_website.split("//")[-1].split(".")[0].capitalize()
    
    # Create a mock response with a well-structured markdown format
    mock_text = f"""
# Source Company Overview
{company_name} is a pharmaceutical company specializing in generic medications and APIs. They focus on cardiovascular, oncology, and central nervous system therapeutics.

# Product Portfolio Summary
- Generic APIs for cardiovascular treatments
- Oncology formulations
- CNS therapeutics
- Contract manufacturing services

# Ideal Customer Profile
Small to mid-size pharmaceutical manufacturers looking for reliable API suppliers, particularly those focused on cardiovascular and oncology products. Regional distributors in emerging markets are also ideal targets.

# Recommended Target Companies Table
| Company Name | Website | Country/Region | Target Segment | Key Contacts | Reason for Recommendation |
| ------------ | ------- | -------------- | ------------- | ------------ | ------------------------- |
| Pharma Solutions Inc. | https://pharmasolutions.example.com | USA | Generic Manufacturer | John Smith, Procurement Director | Needs reliable API suppliers for cardiovascular products |
| MediCorp | https://medicorp.example.com | Germany | Distributor | Maria Schmidt, CEO | Expanding distribution network in Europe for oncology products |
| BioTech Innovations | https://biotechinnovations.example.com | India | Formulation Developer | Raj Patel, Head of R&D | Developing new formulations requiring high-quality APIs |
| HealthCare Partners | https://healthcarepartners.example.com | Brazil | Regional Distributor | Carlos Santos, Business Development | Looking to expand product portfolio in Latin America |
"""
    
    # Create a response structure that matches the Perplexity API response
    mock_response = {
        "id": "mock-response-id",
        "model": "mock-model",
        "created": int(datetime.now().timestamp()),
        "usage": {
            "prompt_tokens": 100,
            "completion_tokens": 500,
            "total_tokens": 600
        },
        "choices": [
            {
                "index": 0,
                "finish_reason": "stop",
                "message": {
                    "role": "assistant",
                    "content": mock_text
                }
            }
        ],
        "text": mock_text  # Add the text field for compatibility with existing code
    }
    
    return mock_response


# Simple in-memory cache (replace with Redis in production)
_cache = {}

def run_deep_research_with_cache(
    prompt: str, 
    max_tokens: Optional[int] = None, 
    cache_ttl_hours: int = 24
) -> Dict[str, Any]:
    """
    Execute a deep research query using the Perplexity API with caching.
    
    Args:
        prompt: The research prompt to send to Perplexity
        max_tokens: Optional maximum number of tokens for the response
        cache_ttl_hours: Time-to-live for cache entries in hours
        
    Returns:
        The JSON response from the Perplexity API
    """
    # Generate cache key from prompt and max_tokens
    cache_key = hashlib.md5(f"{prompt}:{max_tokens}".encode()).hexdigest()
    
    # Check cache
    now = datetime.now()
    if cache_key in _cache:
        cached_result, timestamp = _cache[cache_key]
        if now - timestamp < timedelta(hours=cache_ttl_hours):
            logger.info(f"Cache hit for key: {cache_key[:8]}...")
            return cached_result
    
    # Execute API call
    logger.info(f"Cache miss for key: {cache_key[:8]}...")
    result = run_deep_research(prompt, max_tokens)
    
    # Update cache
    _cache[cache_key] = (result, now)
    
    return result
