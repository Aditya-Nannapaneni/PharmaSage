# PharmaSage v0.1.0 Release Notes

## Overview

This is the initial release of PharmaSage with backend implementation. PharmaSage is a pharmaceutical market intelligence platform that helps pharmaceutical companies discover new markets, find potential buyers, and manage contact intelligence.

## Key Features

- **Backend API Implementation**
  - Dashboard API for metrics and trends
  - Search API for products and companies
  - Match API for prospect discovery
  - Contacts API for contact intelligence

- **Testing Infrastructure**
  - Comprehensive test suite with unit, API, and integration tests
  - Automated test runner script

- **Docker Support**
  - Containerized deployment with Docker
  - Multi-container setup with docker-compose

- **Development Tools**
  - Scripts for development and production environments
  - Environment variable management

## Installation

1. Clone the repository
2. Copy `.env.example` to `.env` and configure environment variables
3. Run `./run_pharmasage.sh` for production mode or `./run_pharmasage_dev.sh` for development mode

## Documentation

See `BUILD_AND_RUN.md` for detailed build and run instructions.

## Changes

For a detailed list of changes, see the [CHANGELOG.md](CHANGELOG.md) file.
