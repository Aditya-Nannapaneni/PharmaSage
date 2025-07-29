# PharmaSage v0.2.0 Release Notes

## Overview

This release introduces AI-powered buyer discovery capabilities to PharmaSage through integration with the Perplexity API. The platform now offers deep research capabilities to identify potential buyers for pharmaceutical products based on company websites and market data.

## Key Features

### AI-Powered Buyer Discovery
- **Perplexity API Integration**: Leverages Perplexity's deep research capabilities to analyze company websites and identify potential buyers
- **Intelligent Parsing**: Robust extraction of company information, business models, and buyer recommendations
- **Caching System**: Efficient caching mechanism to reduce API calls and improve performance
- **Error Handling**: Comprehensive error handling for API interactions with detailed logging

### Enhanced User Experience
- **Interactive Research Interface**: User-friendly interface for initiating and viewing research results
- **Multiple View Options**: Card, table, and detailed views for research results
- **Opportunity Scoring**: Automatic scoring of potential buyers based on fit and potential
- **Contact Intelligence**: Extraction of key contacts from research results

### Developer Improvements
- **Prompt Management System**: Structured approach to managing AI prompts
- **Robust Parsing Framework**: Flexible parsing system that handles various response formats
- **Multiple Fallback Strategies**: Ensures data extraction even when primary methods fail
- **Comprehensive Logging**: Detailed logging for debugging and monitoring

## Technical Enhancements

- **Perplexity API Client**: New client with caching, error handling, and response processing
- **Buyer Research Service**: Service layer for researching and processing potential buyers
- **Research API Endpoints**: New endpoints for initiating research and retrieving results
- **Prompt Management**: Structured approach to managing and versioning AI prompts
- **Response Parsing**: Robust parsing of API responses with multiple extraction strategies

## Bug Fixes

- **API Response Parsing**: Fixed issues with parsing different response formats from the Perplexity API
- **Data Extraction**: Improved extraction of company information and buyer recommendations
- **Frontend Compatibility**: Ensured consistent output format for frontend display
- **Static Files Mounting**: Enhanced to check for dist directory in both current and parent directories

## Installation and Upgrade

1. Pull the latest changes from the repository
2. Update your `.env` file with the new Perplexity API key (see `.env.example` for reference)
3. Run `./run_pharmasage.sh` for production mode or `./run_pharmasage_dev.sh` for development mode

## Configuration

To enable the Perplexity API integration, add the following to your `.env` file:

```
# Perplexity API settings
PERPLEXITY_API_KEY=your_perplexity_api_key

# Mock data control (set to false to use the real API)
USE_MOCK_RESPONSES=false
```

## Documentation

For a detailed list of all changes, see the [CHANGELOG.md](CHANGELOG.md) file.

## Previous Versions

### v0.1.0 - Initial Release

- Backend implementation with FastAPI
- Testing infrastructure
- Docker support
- Development tools
- Documentation
