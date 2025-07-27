"""
Buyer research service.

This module provides services for researching potential buyers using the Perplexity API.
"""
import logging
import re
from typing import Dict, List, Any, Optional
from sqlalchemy.orm import Session

from app.prompts.buyer_discovery import PROSPECT_IDENTIFICATION_PROMPT
from app.services.perplexity_client import run_deep_research_with_cache

# Configure logging
logger = logging.getLogger(__name__)

def format_prompt_with_company_data(company_website: str) -> str:
    """
    Format the prompt template with company data.
    
    Args:
        company_website: The website URL of the company
        
    Returns:
        Formatted prompt ready to be sent to Perplexity API
    """
    # Our prompt is already structured for this use case
    # We just need to replace the placeholder with the actual website
    formatted_prompt = PROSPECT_IDENTIFICATION_PROMPT.replace(
        "<source_company_url>", company_website
    )
    return formatted_prompt

def extract_section_from_markdown(markdown_text: str, section_title: str) -> Optional[str]:
    """
    Extract a specific section from markdown text.
    
    Args:
        markdown_text: The markdown text to parse
        section_title: The title of the section to extract
        
    Returns:
        The extracted section text, or None if not found
    """
    # Simple regex pattern to find sections by heading
    # This pattern captures content until the next heading of the same or higher level
    pattern = rf"#+\s*{re.escape(section_title)}.*?\n(.*?)(?=\n#+\s*|$)"
    match = re.search(pattern, markdown_text, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    
    return None

def parse_markdown_table(table_text: str) -> List[Dict[str, str]]:
    """
    Parse a markdown table into a list of dictionaries.
    
    Args:
        table_text: The markdown table text
        
    Returns:
        List of dictionaries, each representing a row in the table
    """
    lines = table_text.strip().split('\n')
    
    # Need at least header, separator, and one data row
    if len(lines) < 3:
        return []
    
    # Extract headers
    headers = [h.strip() for h in re.split(r'\s*\|\s*', lines[0].strip('|'))]
    
    # Skip the separator line
    data_rows = []
    for line in lines[2:]:
        if not line.strip():
            continue
            
        # Split the line by pipe character and strip whitespace
        values = [v.strip() for v in re.split(r'\s*\|\s*', line.strip('|'))]
        
        # Create a dictionary for this row
        if len(values) == len(headers):
            row_dict = {headers[i]: values[i] for i in range(len(headers))}
            data_rows.append(row_dict)
    
    return data_rows

def parse_research_results(research_response: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Parse the markdown response from Perplexity into structured prospect data.
    
    Args:
        research_response: The response from the Perplexity API
        
    Returns:
        List of prospect dictionaries
    """
    # Extract the text content from the response
    if "text" not in research_response:
        logger.error("Unexpected response format from Perplexity API")
        return []
    
    markdown_text = research_response["text"]
    
    # Extract the recommended targets table section
    table_section = extract_section_from_markdown(markdown_text, "Recommended Target Companies Table")
    if not table_section:
        logger.warning("Could not find recommended targets table in research results")
        return []
    
    # Parse the markdown table
    table_data = parse_markdown_table(table_section)
    
    # Convert table data to prospect format
    prospects = []
    for i, row in enumerate(table_data):
        # Map table columns to prospect fields
        prospect = {
            "id": f"research-{i+1}",
            "name": row.get("Company Name", "Unknown Company"),
            "location": row.get("Country/Region", "Unknown Location"),
            "segment": row.get("Target Segment", "Unknown Segment"),
            "website": row.get("Website", ""),
            "keyContacts": [row.get("Key Contacts", "")] if row.get("Key Contacts") else [],
            "reasonForRecommendation": row.get("Reason for Recommendation", ""),
            "opportunityScore": 75,  # Default score for research-based prospects
            "status": "Research",
            "source": "perplexity_research"
        }
        prospects.append(prospect)
    
    return prospects

def research_potential_buyers(
    db: Session, 
    company_name: str,
    company_website: str,
    products: List[str]
) -> List[Dict[str, Any]]:
    """
    Research potential buyers for a company using Perplexity Deep Research.
    
    Args:
        db: Database session
        company_name: Name of the company
        company_website: Website URL of the company
        products: List of product names
        
    Returns:
        List of potential buyer prospects with details
    """
    logger.info(f"Researching potential buyers for {company_name} ({company_website})")
    
    try:
        # Format the prompt with the company website
        formatted_prompt = format_prompt_with_company_data(company_website)
        
        # Execute the deep research query with caching
        research_response = run_deep_research_with_cache(formatted_prompt)
        
        # Parse the results into structured data
        prospects = parse_research_results(research_response)
        
        logger.info(f"Found {len(prospects)} potential buyers through research")
        return prospects
        
    except Exception as e:
        logger.error(f"Error researching potential buyers: {str(e)}")
        raise Exception(f"Failed to research potential buyers: {str(e)}")
