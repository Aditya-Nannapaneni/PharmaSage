# PharmaSage Prompts

This directory contains prompt templates used by PharmaSage AI services.

## Directory Structure

```
prompts/
├── __init__.py                      # Package initialization
├── base.py                          # Base utilities and classes
├── README.md                        # This file
└── buyer_discovery/                 # Buyer discovery prompts
    ├── __init__.py                  # Exports buyer discovery prompts
    └── prospect_identification.py   # Prospect identification prompt
```

## Usage

To use a prompt in a service:

```python
from app.prompts.buyer_discovery import PROSPECT_IDENTIFICATION_PROMPT

def find_prospects(db, company_name, products, licensed_markets, limit):
    # Get company website from database
    company = db.query(Company).filter(Company.name == company_name).first()
    company_website = company.website if company else None
    
    if not company_website:
        return {"error": "Company website not found"}
    
    # Call LLM with prompt
    response = call_llm_with_prompt(
        PROSPECT_IDENTIFICATION_PROMPT,
        source_company_url=company_website
    )
    
    # Process response and return results
    # ...
```

## Adding New Prompts

1. Create a new file in the appropriate subdirectory
2. Define your prompt as a constant
3. Export the prompt in the subdirectory's `__init__.py`
4. Use the prompt in your service

## Prompt Design Guidelines

- Use clear, concise language
- Structure prompts with sections for better organization
- Include examples where helpful
- Document the expected input and output format
