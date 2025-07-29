# Changelog

All notable changes to the PharmaSage project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Perplexity API integration for deep research on potential buyers
  - New Perplexity API client with caching and error handling
  - Buyer research service for identifying potential buyers
  - Research API endpoints for direct access to research functionality
  - Enhanced matching service to include research-based prospects
  - Customized outreach guidance for research-based prospects
  - Comprehensive unit tests for all new components
- Prompt management structure for AI services
  - Base prompt template utilities
  - Buyer discovery prospect identification prompt
  - Documentation for prompt management

### Fixed
- Enhanced static files mounting to check for dist directory in both current and parent directories
  - Resolves issue where backend server couldn't find static files when run from backend directory
  - Adds improved logging for static files mounting
- Improved Perplexity API response parsing in buyer research service
  - Fixed handling of different response formats from the Perplexity API
  - Added robust extraction methods for company information
  - Implemented multiple fallback strategies for data extraction
  - Enhanced error handling and logging for better debugging
  - Ensured consistent output format for frontend compatibility

## [0.1.0] - 2025-07-23

### Added
- Backend implementation with FastAPI
  - API endpoints for dashboard, search, match, and contacts
  - Database models for companies, products, contacts, licenses, and transactions
  - Service layer for business logic
  - Database session management with SQLAlchemy
  - Configuration management with Pydantic
- Testing infrastructure
  - Integration tests with test_app.py
  - API tests with test_api.py
  - Service unit tests with test_services.py
  - Test runner script (run_tests.sh)
- Docker configuration
  - Dockerfile for containerized deployment
  - docker-compose.yml for multi-container setup
- Build and run scripts
  - run_pharmasage.sh for production mode
  - run_pharmasage_dev.sh for development mode
  - backend_start.sh for backend development
- Documentation
  - BUILD_AND_RUN.md with build and run instructions
  - .env.example with example environment variables

### Changed
- Removed Compliance Monitoring feature
- Updated landing page to remove Compliance Monitoring references
- Updated navigation to remove Compliance Monitoring route

### Fixed
- Fixed configuration to work with newer version of Pydantic
- Fixed database session management to handle PostgresDsn objects
- Fixed static files mounting to check if directory exists
