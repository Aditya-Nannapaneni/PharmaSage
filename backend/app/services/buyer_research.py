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
    
    # Log if section not found
    logger.info(f"Section '{section_title}' not found in markdown text")
    return None

def parse_markdown_table(table_text: str) -> List[Dict[str, str]]:
    """
    Parse a markdown table into a list of dictionaries.
    
    Args:
        table_text: The markdown table text
        
    Returns:
        List of dictionaries, each representing a row in the table
    """
    if not table_text:
        logger.info("Table text is empty")
        return []
        
    lines = table_text.strip().split('\n')
    
    # Need at least header, separator, and one data row
    if len(lines) < 3:
        logger.info(f"Table has insufficient lines: {len(lines)}")
        return []
    
    # Extract headers
    headers = [h.strip() for h in re.split(r'\s*\|\s*', lines[0].strip('|'))]
    logger.info(f"Table headers: {headers}")
    
    # Skip the separator line
    data_rows = []
    for line in lines[2:]:
        if not line.strip():
            continue
            
        # Split the line by pipe character and strip whitespace
        values = [v.strip() for v in re.split(r'\s*\|\s*', line.strip('|'))]
        logger.info(f"Table row values: {values}")
        
        # Create a dictionary for this row
        if len(values) == len(headers):
            row_dict = {headers[i]: values[i] for i in range(len(headers))}
            data_rows.append(row_dict)
        else:
            logger.warning(f"Mismatch between headers ({len(headers)}) and values ({len(values)})")
    
    return data_rows

def parse_research_results(research_response: Dict[str, Any], company_name: str, company_website: str) -> Dict[str, Any]:
    """
    Parse the response from Perplexity API into structured research data.
    
    This function extracts relevant information from the Perplexity API response,
    which may contain content in different formats, and structures it for frontend display.
    
    Args:
        research_response: The response from the Perplexity API
        company_name: Name of the company
        company_website: Website URL of the company
        
    Returns:
        Dictionary with source company info, ideal customer profile, and discovered buyers
    """
    # Extract the text content from the response
    markdown_text = ""
    
    # First try to get content from the choices array (new API format)
    if "choices" in research_response and len(research_response["choices"]) > 0:
        if "message" in research_response["choices"][0] and "content" in research_response["choices"][0]["message"]:
            logger.info("Found content in choices[0].message.content")
            markdown_text = research_response["choices"][0]["message"]["content"]
    # Fall back to text field if available (old format or added by client)
    elif "text" in research_response:
        markdown_text = research_response["text"]
    
    if not markdown_text:
        logger.error("No content found in Perplexity API response")
        logger.error(f"Response keys: {research_response.keys()}")
        raise Exception("Failed to extract content from research response")
    
    # Log the markdown text length for debugging
    logger.info(f"Markdown text length: {len(markdown_text)}")
    
    # Remove the <think> section if present
    think_pattern = r"<think>.*?</think>"
    markdown_text = re.sub(think_pattern, "", markdown_text, flags=re.DOTALL)
    
    # Parse the content based on structure
    # First, try to extract sections using headers
    sections = {}
    
    # Try to extract sections using different header patterns
    section_patterns = [
        # Standard markdown headers
        r"#+\s*(.*?)\s*\n(.*?)(?=\n#+\s*|$)",
        # Sections with horizontal rules
        r"(.*?)\n-{3,}\s*\n(.*?)(?=\n.*?\n-{3,}|$)",
        # Bold headers
        r"\*\*(.*?)\*\*\s*\n(.*?)(?=\n\*\*.*?\*\*|$)"
    ]
    
    for pattern in section_patterns:
        matches = re.finditer(pattern, markdown_text, re.DOTALL)
        for match in matches:
            section_title = match.group(1).strip()
            section_content = match.group(2).strip()
            sections[section_title.lower()] = section_content
    
    # Extract company overview
    overview = ""
    overview_keys = ["overview", "source company overview", "company overview", "sequent"]
    for key in overview_keys:
        if key in sections:
            overview = sections[key]
            break
    
    # If no overview section found, use the first paragraph
    if not overview:
        paragraphs = re.split(r'\n\s*\n', markdown_text)
        if paragraphs:
            overview = paragraphs[0].strip()
    
    # Extract business model and therapeutic coverage
    business_model = ""
    business_model_keys = ["business model", "product portfolio", "product portfolio summary"]
    for key in business_model_keys:
        if key in sections:
            business_model = sections[key]
            break
    
    therapeutic_coverage = ""
    therapeutic_keys = ["therapeutic coverage", "therapeutic areas", "therapeutic focus"]
    for key in therapeutic_keys:
        if key in sections:
            therapeutic_coverage = sections[key]
            break
    
    # If therapeutic coverage not found, use business model
    if not therapeutic_coverage:
        therapeutic_coverage = business_model
    
    # Extract ideal customer profile
    ideal_customer = ""
    ideal_customer_keys = ["ideal customer profile", "target customer", "customer profile"]
    for key in ideal_customer_keys:
        if key in sections:
            ideal_customer = sections[key]
            break
    
    # Extract potential buyers
    # First try to find a table in the markdown
    table_pattern = r"\|.*\|.*\|\n\|[-:\s|]+\|\n(\|.*\|.*\|\n)+"
    table_match = re.search(table_pattern, markdown_text, re.MULTILINE)
    
    prospects = []
    
    if table_match:
        # Parse the markdown table
        table_section = table_match.group(0)
        table_data = parse_markdown_table(table_section)
        
        # Convert table data to prospect format
        for i, row in enumerate(table_data):
            prospect = {
                "id": f"research-{i+1}",
                "name": row.get("Company Name", "Unknown Company"),
                "country": row.get("Country/Region", "Unknown Location"),
                "region": row.get("Country/Region", "").split("/")[1].strip() if "/" in row.get("Country/Region", "") else "",
                "targetSegment": row.get("Target Segment", "Unknown Segment"),
                "website": row.get("Website", ""),
                "keyContacts": [],
                "reasonForRecommendation": row.get("Reason for Recommendation", ""),
                "opportunityScore": 75,  # Default score for research-based prospects
                "status": "Research"
            }
            
            # Process key contacts
            key_contacts_str = row.get("Key Contacts", "")
            if key_contacts_str:
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
    else:
        # No table found, try to extract company information from sections
        # Look for numbered lists or sections that might contain company information
        company_section_pattern = r"(?:(?:\d+\.\s*\*\*([^*]+)\*\*)|(?:###\s*(\d+\.\s*[^#\n]+)))"
        company_matches = re.finditer(company_section_pattern, markdown_text, re.MULTILINE)
        
        company_names = []
        for i, match in enumerate(company_matches):
            company_name = match.group(1) if match.group(1) else match.group(2)
            if company_name:
                company_names.append(company_name.strip())
        
        # If we found company names, create prospects
        for i, name in enumerate(company_names):
            # Try to find website for this company
            website = ""
            website_pattern = rf"{re.escape(name)}.*?(?:Website|URL|site):\s*\[?([^\s\]]+)"
            website_match = re.search(website_pattern, markdown_text, re.IGNORECASE | re.DOTALL)
            if website_match:
                website = website_match.group(1)
            
            # Try to find reason for recommendation
            reason = ""
            reason_pattern = rf"{re.escape(name)}.*?(?:Reason|Fit|Rationale).*?\n(.*?)(?=\n\d+\.|\n###|\Z)"
            reason_match = re.search(reason_pattern, markdown_text, re.IGNORECASE | re.DOTALL)
            if reason_match:
                reason = reason_match.group(1).strip()
            
            prospect = {
                "id": f"research-{i+1}",
                "name": name,
                "country": "Unknown Location",
                "region": "",
                "targetSegment": "Pharmaceutical",
                "website": website,
                "keyContacts": [],
                "reasonForRecommendation": reason,
                "opportunityScore": 75,
                "status": "Research"
            }
            
            prospects.append(prospect)
    
    # If no prospects were found through either method, extract from the structured sections
    if not prospects:
        # Look for sections that might contain company information
        potential_buyer_sections = ["recommended target companies", "potential buyers", "target companies"]
        
        for section_key in potential_buyer_sections:
            if section_key in sections:
                section_content = sections[section_key]
                
                # Try to extract company names with numbered or bulleted lists
                company_pattern = r"(?:^|\n)(?:\d+\.|\*)\s*([^:\n]+)(?::|$)"
                company_matches = re.finditer(company_pattern, section_content, re.MULTILINE)
                
                for i, match in enumerate(company_matches):
                    company_name = match.group(1).strip()
                    if company_name:
                        # Try to extract website
                        website = ""
                        website_pattern = rf"{re.escape(company_name)}.*?(?:Website|URL|site):\s*([^\s,]+)"
                        website_match = re.search(website_pattern, section_content, re.IGNORECASE | re.DOTALL)
                        if website_match:
                            website = website_match.group(1)
                        
                        # Try to extract reason
                        reason = ""
                        reason_pattern = rf"{re.escape(company_name)}.*?(?:Reason|Fit|Rationale).*?:\s*(.*?)(?=\n\d+\.|\n\*|\Z)"
                        reason_match = re.search(reason_pattern, section_content, re.IGNORECASE | re.DOTALL)
                        if reason_match:
                            reason = reason_match.group(1).strip()
                        
                        prospect = {
                            "id": f"research-{i+1}",
                            "name": company_name,
                            "country": "Unknown Location",
                            "region": "",
                            "targetSegment": "Pharmaceutical",
                            "website": website,
                            "keyContacts": [],
                            "reasonForRecommendation": reason,
                            "opportunityScore": 75,
                            "status": "Research"
                        }
                        
                        prospects.append(prospect)
    
    # If still no prospects, extract from the example in the response
    if not prospects:
        # Extract company names from the response using regex patterns
        company_patterns = [
            r"\*\*(\d+\.\s*[^*]+)\*\*",  # Bold numbered items
            r"###\s*(\d+\.\s*[^#\n]+)",  # H3 headers with numbers
            r"(?:^|\n)(\d+\.\s*[A-Z][^:\n]+)(?::|$)",  # Numbered items starting with capital letter
            r"(?:^|\n)(\*\s*[A-Z][^:\n]+)(?::|$)"  # Bulleted items starting with capital letter
        ]
        
        extracted_companies = []
        for pattern in company_patterns:
            matches = re.finditer(pattern, markdown_text, re.MULTILINE)
            for match in matches:
                company_name = match.group(1).strip()
                # Clean up the company name (remove numbering, etc.)
                company_name = re.sub(r"^\d+\.\s*", "", company_name)
                company_name = re.sub(r"^\*\s*", "", company_name)
                
                if company_name and len(company_name) > 3:  # Avoid very short names
                    extracted_companies.append(company_name)
        
        # Create prospects from extracted company names
        for i, name in enumerate(extracted_companies):
            # Try to find website using regex
            website = ""
            website_pattern = rf"(?:{re.escape(name)}|Website).*?(?:https?://[^\s,)]+)"
            website_match = re.search(website_pattern, markdown_text, re.IGNORECASE | re.DOTALL)
            if website_match:
                website = website_match.group(1)
            
            prospect = {
                "id": f"research-{i+1}",
                "name": name,
                "country": "Unknown Location",
                "region": "",
                "targetSegment": "Pharmaceutical",
                "website": website,
                "keyContacts": [],
                "reasonForRecommendation": f"Potential buyer for {company_name}'s products",
                "opportunityScore": 75,
                "status": "Research"
            }
            
            prospects.append(prospect)
    
    # Construct the full research results
    research_results = {
        "sourceCompany": {
            "name": company_name,
            "url": company_website,
            "overview": overview,
            "businessModel": business_model,
            "therapeuticCoverage": therapeutic_coverage
        },
        "idealCustomerProfile": ideal_customer,
        "discoveredBuyers": prospects
    }
    
    logger.info(f"Found {len(prospects)} potential buyers through research")
    return research_results

def research_potential_buyers(
    db: Session, 
    company_name: str,
    company_website: str
) -> Dict[str, Any]:
    """
    Research potential buyers for a company using Perplexity Deep Research.
    
    Args:
        db: Database session
        company_name: Name of the company
        company_website: Website URL of the company
        
    Returns:
        Dictionary with source company info, ideal customer profile, and discovered buyers
    """
    logger.info(f"Researching potential buyers for {company_name} ({company_website})")
    
    try:
        # Format the prompt with the company website
        formatted_prompt = format_prompt_with_company_data(company_website)
        
        # Execute the deep research query with caching
        research_response = run_deep_research_with_cache(formatted_prompt)
        
        # Log the response structure
        logger.info(f"Research response keys: {research_response.keys()}")
        
        # Parse the results into structured data
        research_results = parse_research_results(research_response, company_name, company_website)
        
        logger.info(f"Found {len(research_results['discoveredBuyers'])} potential buyers through research")
        return research_results
        
    except Exception as e:
        logger.error(f"Error researching potential buyers: {str(e)}")
        raise Exception(f"Failed to research potential buyers: {str(e)}")
