#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print status messages
print_status() {
  echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
  echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
  echo -e "${RED}[ERROR]${NC} $1"
}

print_status "Running PharmaSage Backend Tests"
print_status "================================"

# Check if we're in the backend directory
if [ ! -f "app/main.py" ]; then
  print_warning "This script should be run from the backend directory."
  print_warning "Changing to the backend directory..."
  cd backend 2>/dev/null || { print_error "Could not find backend directory. Make sure you're in the project root."; exit 1; }
fi

# Check for Python
if ! command -v python3 &> /dev/null; then
  print_error "Python 3 is not installed. Please install Python 3 and try again."
  exit 1
fi

# Check for virtual environment
if [ ! -d "venv" ]; then
  print_status "Creating Python virtual environment..."
  python3 -m venv venv
  source venv/bin/activate
  print_status "Installing dependencies..."
  pip install -r requirements.txt
else
  print_status "Activating virtual environment..."
  source venv/bin/activate
fi

# Run the integration test
print_status "\nRunning Integration Test (test_app.py)..."
print_status "----------------------------------------"
python test_app.py

# Run the service unit tests
print_status "\nRunning Service Unit Tests (test_services.py)..."
print_status "----------------------------------------------"
python test_services.py

# Run the API tests
print_status "\nRunning API Tests (test_api.py)..."
print_status "-----------------------------------"
python test_api.py

print_status "\nAll tests completed!"
print_status "To run individual tests, use:"
print_status "  python test_app.py      # Integration test"
print_status "  python test_services.py # Service unit tests"
print_status "  python test_api.py      # API tests"

# Deactivate virtual environment
deactivate
