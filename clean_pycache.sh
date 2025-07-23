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

print_status "Counting Python cache files before cleanup..."
PYCACHE_COUNT=$(find . -type d -name "__pycache__" | wc -l)
PYC_COUNT=$(find . -name "*.pyc" | wc -l)
PYO_COUNT=$(find . -name "*.pyo" | wc -l)
PYD_COUNT=$(find . -name "*.pyd" | wc -l)
TOTAL_COUNT=$((PYCACHE_COUNT + PYC_COUNT + PYO_COUNT + PYD_COUNT))
print_status "Found $PYCACHE_COUNT __pycache__ directories and $((PYC_COUNT + PYO_COUNT + PYD_COUNT)) .pyc/.pyo/.pyd files."

print_status "Cleaning up Python cache files..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete
find . -name "*.pyo" -delete
find . -name "*.pyd" -delete
print_status "Python cache files removed."

print_status "Cleanup complete! Removed approximately $TOTAL_COUNT files/directories."
print_status "You can now commit your changes with:"
print_status "git add ."
print_status "git commit -m \"Your commit message\""
