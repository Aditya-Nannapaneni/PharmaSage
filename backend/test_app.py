"""
Simple test script for PharmaSage backend.

This script tests the basic functionality of the PharmaSage backend API.
"""
import asyncio
import httpx
import uvicorn
import threading
import time
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add the parent directory to the path so we can import the app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import after path setup
from app.db.base import Base
from app.main import app

# Create an in-memory SQLite database for testing
TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the database session in the app
from app.db.session import get_db

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


async def test_api():
    """Test the API endpoints."""
    # Create database tables
    Base.metadata.create_all(bind=engine)
    
    # Start the server in a separate thread
    server_thread = threading.Thread(
        target=lambda: uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
    )
    server_thread.daemon = True
    server_thread.start()
    
    # Wait for server to start
    time.sleep(2)
    
    # Test API endpoints
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        print("\n=== Testing Dashboard API ===")
        # Test dashboard trends endpoint
        response = await client.get("/api/dashboard/trends")
        print(f"Dashboard trends response: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Global trade volume: {data.get('global_trade_volume', {}).get('value')} {data.get('global_trade_volume', {}).get('unit')}")
            print(f"Active products: {data.get('active_products', {}).get('value')}")
            print(f"Export companies: {data.get('export_companies', {}).get('value')}")
            print(f"Active markets: {data.get('active_markets', {}).get('value')}")
        
        print("\n=== Testing Search API ===")
        # Test search products endpoint
        response = await client.get("/api/search/products?query=paracetamol")
        print(f"Search products response: {response.status_code}")
        if response.status_code == 200:
            products = response.json()
            print(f"Found {len(products)} products matching 'paracetamol'")
            for product in products[:3]:  # Show first 3 products
                print(f"- {product.get('api_name')} ({product.get('form')})")
        
        print("\n=== Testing Match API ===")
        # Test prospect matching endpoint
        response = await client.post(
            "/api/match/prospects",
            json={
                "company_name": "Test Pharma",
                "products": ["Paracetamol", "Ibuprofen"],
                "licensed_markets": ["Europe", "North America"]
            }
        )
        print(f"Match prospects response: {response.status_code}")
        if response.status_code == 200:
            prospects = response.json()
            print(f"Found {len(prospects)} potential prospects")
            for prospect in prospects[:3]:  # Show first 3 prospects
                print(f"- {prospect.get('name')} ({prospect.get('location')}) - Score: {prospect.get('opportunityScore')}")
        
        print("\n=== Testing Contacts API ===")
        # Test prospect contacts endpoint
        response = await client.get("/api/prospect/1/contacts")
        print(f"Prospect contacts response: {response.status_code}")
        if response.status_code == 200:
            contacts = response.json()
            print(f"Found {len(contacts)} contacts")
            for contact in contacts[:3]:  # Show first 3 contacts
                print(f"- {contact.get('name')} ({contact.get('role')})")
        
        # Test contact stats endpoint
        response = await client.get("/api/prospect/stats")
        print(f"Contact stats response: {response.status_code}")
        if response.status_code == 200:
            stats = response.json()
            print(f"Total contacts: {stats.get('total_contacts')}")
            print(f"Key contacts: {stats.get('key_contacts')}")
            print(f"Recent interactions: {stats.get('recent_interactions')}")
            print(f"Companies: {stats.get('companies')}")
    
    print("\nAll tests completed!")


if __name__ == "__main__":
    asyncio.run(test_api())
