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

def parse_research_results(research_response: Dict[str, Any], company_name: str, company_website: str) -> Dict[str, Any]:
    """
    Parse the markdown response from Perplexity into structured research data.
    
    Args:
        research_response: The response from the Perplexity API
        company_name: Name of the company
        company_website: Website URL of the company
        
    Returns:
        Dictionary with source company info, ideal customer profile, and discovered buyers
    """
    # Extract the text content from the response
    if "text" not in research_response:
        logger.error("Unexpected response format from Perplexity API")
        return {
            "sourceCompany": {
                "name": company_name,
                "url": company_website,
                "overview": "Could not retrieve company overview.",
                "businessModel": "Could not retrieve business model.",
                "therapeuticCoverage": "Could not retrieve therapeutic coverage."
            },
            "idealCustomerProfile": "Could not retrieve ideal customer profile.",
            "discoveredBuyers": []
        }
    
    markdown_text = research_response["text"]
    
    # Extract sections from the markdown text
    source_company_overview = extract_section_from_markdown(markdown_text, "Source Company Overview") or "No company overview available."
    product_portfolio = extract_section_from_markdown(markdown_text, "Product Portfolio Summary") or "No product portfolio available."
    ideal_customer_profile = extract_section_from_markdown(markdown_text, "Ideal Customer Profile") or "No ideal customer profile available."
    table_section = extract_section_from_markdown(markdown_text, "Recommended Target Companies Table")
    
    # Parse the markdown table
    table_data = parse_markdown_table(table_section) if table_section else []
    
    # Convert table data to prospect format
    prospects = []
    for i, row in enumerate(table_data):
        # Map table columns to prospect fields with exact frontend-expected field names
        prospect = {
            "id": f"research-{i+1}",
            "name": row.get("Company Name", "Unknown Company"),
            "country": row.get("Country/Region", "Unknown Location"),  # Changed from "location" to "country"
            "region": row.get("Country/Region", "").split("/")[1].strip() if "/" in row.get("Country/Region", "") else "",
            "targetSegment": row.get("Target Segment", "Unknown Segment"),  # Changed from "segment" to "targetSegment"
            "website": row.get("Website", ""),
            "keyContacts": [],
            "reasonForRecommendation": row.get("Reason for Recommendation", ""),
            "opportunityScore": 75,  # Default score for research-based prospects
            "status": "Research"
        }
        
        # Process key contacts - handle both string and structured formats
        key_contacts_str = row.get("Key Contacts", "")
        if key_contacts_str:
            # Simple parsing for "Name, Role" format
            contacts = []
            for contact_str in key_contacts_str.split(";"):
                contact_str = contact_str.strip()
                if "," in contact_str:
                    name, role = contact_str.split(",", 1)
                    contacts.append({"name": name.strip(), "role": role.strip()})
                else:
                    contacts.append({"name": contact_str, "role": ""})
            prospect["keyContacts"] = contacts
        
        prospects.append(prospect)
    
    # Construct the full research results
    research_results = {
        "sourceCompany": {
            "name": company_name,
            "url": company_website,
            "overview": source_company_overview,
            "businessModel": product_portfolio,
            "therapeuticCoverage": product_portfolio
        },
        "idealCustomerProfile": ideal_customer_profile,
        "discoveredBuyers": prospects
    }
    
    return research_results

def research_potential_buyers(
    db: Session, 
    company_name: str,
    company_website: str,
    products: List[str]
) -> Dict[str, Any]:
    """
    Research potential buyers for a company using Perplexity Deep Research.
    
    Args:
        db: Database session
        company_name: Name of the company
        company_website: Website URL of the company
        products: List of product names
        
    Returns:
        Dictionary with source company info, ideal customer profile, and discovered buyers
    """
    logger.info(f"Researching potential buyers for {company_name} ({company_website})")
    
    try:
        # Format the prompt with the company website
        formatted_prompt = format_prompt_with_company_data(company_website)
        
        # Execute the deep research query with caching
        research_response = run_deep_research_with_cache(formatted_prompt)
        
        # Parse the results into structured data
        research_results = parse_research_results(research_response, company_name, company_website)
        
        logger.info(f"Found {len(research_results['discoveredBuyers'])} potential buyers through research")
        return research_results
        
    except Exception as e:
        logger.error(f"Error researching potential buyers: {str(e)}")
        raise Exception(f"Failed to research potential buyers: {str(e)}")
