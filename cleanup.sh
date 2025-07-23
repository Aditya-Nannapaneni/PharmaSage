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

print_status "Cleaning up Python cache files..."
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -name "*.pyc" -delete
find . -name "*.pyo" -delete
find . -name "*.pyd" -delete
print_status "Python cache files removed."

print_status "Cleaning up virtual environments..."
find . -type d -name "venv" -exec rm -rf {} +
print_status "Virtual environments removed."

print_status "Cleaning up node_modules..."
find . -type d -name "node_modules" -exec rm -rf {} +
print_status "node_modules removed."

print_status "Cleaning up build artifacts..."
find . -type d -name "dist" -exec rm -rf {} +
find . -type d -name "build" -exec rm -rf {} +
print_status "Build artifacts removed."

print_status "Cleanup complete!"
print_status "You can now commit your changes with:"
print_status "git add ."
print_status "git commit -m \"Your commit message\""
