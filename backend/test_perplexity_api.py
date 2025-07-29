#!/usr/bin/env python3
"""
Test script for Perplexity API.

This script tests the Perplexity API directly and saves the response to a file.
"""
import os
import json
import requests
import logging
import argparse
from datetime import datetime
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_api_key(api_key_arg=None):
    """
    Load API key from command line argument, .env file, or prompt user.
    
    Args:
        api_key_arg: API key from command line argument
        
    Returns:
        Tuple of (api_key, use_mock)
    """
    # Try to load from command line argument first
    if api_key_arg:
        logger.info("Using API key from command line argument")
        return api_key_arg, False
    
    # Try to load from .env file in current directory
    load_dotenv()
    
    # If not found, try to load from parent directory
    if not os.getenv("PERPLEXITY_API_KEY"):
        load_dotenv(dotenv_path="../.env")
    
    api_key = os.getenv("PERPLEXITY_API_KEY")
    use_mock = os.getenv("USE_MOCK_RESPONSES", "false").lower() == "true"
    
    logger.info(f"USE_MOCK_RESPONSES: {use_mock}")
    
    # If no API key and not using mock, prompt user
    if not api_key and not use_mock:
        logger.warning("No API key found in .env file")
        api_key = input("Please enter your Perplexity API key: ").strip()
        
        if not api_key:
            logger.error("No API key provided")
            raise ValueError("API key is required to test the Perplexity API")
    
    return api_key, use_mock

def test_perplexity_api(api_key, prompt="Tell me about quantum computing"):
    """
    Test the Perplexity API with a simple prompt.
    
    Args:
        api_key: Perplexity API key
        prompt: The prompt to send to the API
        
    Returns:
        The API response
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Using the correct model name for Perplexity Sonar Deep Research API
    payload = {
        "model": "sonar-deep-research",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    logger.info("Sending request to Perplexity API")
    logger.info(f"Request payload: {json.dumps(payload)}")
    
    try:
        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            json=payload,
            headers=headers
        )
        
        logger.info(f"Response status code: {response.status_code}")
        
        if response.status_code != 200:
            logger.error(f"Error response: {response.text}")
            return None
        
        return response.json()
    
    except Exception as e:
        logger.error(f"Error making API request: {str(e)}")
        return None

def save_response_to_file(response, filename=None):
    """
    Save the API response to a file.
    
    Args:
        response: The API response
        filename: Optional filename to save to
    """
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"perplexity_response_{timestamp}.json"
    
    with open(filename, "w") as f:
        json.dump(response, f, indent=2)
    
    logger.info(f"Response saved to {filename}")
    return filename

def analyze_response(response):
    """
    Analyze the API response and print key information.
    
    Args:
        response: The API response
    """
    if not response:
        logger.error("No response to analyze")
        return
    
    logger.info("Response Analysis:")
    logger.info(f"Model: {response.get('model', 'Unknown')}")
    
    # Check for usage information
    usage = response.get("usage", {})
    if usage:
        logger.info(f"Usage: {json.dumps(usage)}")
    
    # Check for choices/content
    choices = response.get("choices", [])
    if choices and len(choices) > 0:
        message = choices[0].get("message", {})
        content = message.get("content", "")
        logger.info(f"Content length: {len(content)} characters")
        logger.info(f"Content preview: {content[:200]}...")
    else:
        logger.error("No content found in response")
    
    # Check for citations
    citations = response.get("citations", [])
    if citations:
        logger.info(f"Number of citations: {len(citations)}")
        logger.info(f"First few citations: {citations[:3]}")

def main():
    """Main function."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Test the Perplexity API")
    parser.add_argument("--api-key", help="Perplexity API key")
    parser.add_argument("--prompt", help="Prompt to send to the API")
    parser.add_argument("--output", help="Output file name")
    parser.add_argument("--mock", action="store_true", help="Use mock response")
    args = parser.parse_args()
    
    logger.info("Starting Perplexity API test")
    
    try:
        # Override use_mock if --mock flag is provided
        api_key, use_mock = load_api_key(args.api_key)
        if args.mock:
            use_mock = True
        
        if use_mock:
            logger.info("Mock mode is enabled. Using mock response.")
            # Create a mock response for testing
            response = {
                "model": "mock-model",
                "choices": [
                    {
                        "message": {
                            "role": "assistant",
                            "content": "This is a mock response for testing purposes."
                        }
                    }
                ]
            }
        else:
            # Use provided prompt or default
            prompt = args.prompt if args.prompt else """
            Analyze the pharmaceutical company Sequent (https://sequent.in) and identify 
            potential buyers for their products. Include company names, websites, and 
            reasons for recommendation.
            """
            response = test_perplexity_api(api_key, prompt)
        
        if response:
            # Save the response to a file
            filename = args.output if args.output else None
            filename = save_response_to_file(response, filename)
            
            # Analyze the response
            analyze_response(response)
            
            logger.info(f"Test completed successfully. Response saved to {filename}")
            print(f"\nResponse saved to {filename}")
            print("You can use this file for further analysis or debugging.")
        else:
            logger.error("Test failed. No response received.")
    
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")

if __name__ == "__main__":
    main()
