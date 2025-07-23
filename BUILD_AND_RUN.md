# Building and Running PharmaSage Locally

This document provides instructions for building and running the PharmaSage application locally.

## Prerequisites

Before you begin, ensure you have the following installed:

- Node.js (v16 or later)
- npm (v7 or later)
- Python 3.8 or later
- pip3

## Option 1: Using the Automated Scripts

We've provided two scripts to automate the process of building and running PharmaSage:

### Production Build

To build and run the production version of PharmaSage:

```bash
./run_pharmasage.sh
```

This script will:
1. Check if all required dependencies are installed
2. Update the browserslist database
3. Install frontend dependencies if needed
4. Build the frontend
5. Install backend dependencies in a virtual environment if needed
6. Start the backend server, which will serve the frontend from the `dist` directory

Once the script completes successfully, you can access the application at:
```
http://localhost:8000
```

To stop the server, press `Ctrl+C` in the terminal where the script is running.

### Development Mode

For development with hot-reloading:

```bash
./run_pharmasage_dev.sh
```

This script will:
1. Check if all required dependencies are installed
2. Update the browserslist database
3. Install frontend dependencies if needed
4. Install backend dependencies in a virtual environment if needed
5. Start the backend server in a new terminal window
6. Start the frontend development server with hot-reloading

Once the script completes successfully, you can access:
- Frontend: `http://localhost:5173`
- Backend API: `http://localhost:8000/api`
- API Documentation: `http://localhost:8000/api/docs`

#### Stopping the Development Servers

When running in development mode, two servers are started:
1. The frontend server (in the terminal where you ran the script)
2. The backend server (in a separate terminal window)

To stop both servers:
1. Press `Ctrl+C` in the terminal where the frontend server is running
2. Go to the terminal window where the backend server is running and press `Ctrl+C`
3. Alternatively, you can find and kill the backend process:
   ```bash
   # Find the process
   ps aux | grep "uvicorn app.main:app"
   
   # Kill the process (replace <PID> with the process ID from the previous command)
   kill <PID>
   ```

## Option 2: Manual Setup

If you prefer to run the commands manually:

### Frontend Setup

```bash
# Install dependencies
npm install

# Build for production
npm run build

# OR for development with hot-reloading
npm run dev
```

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app.main:app --reload
```

## Testing the Backend

We've provided several scripts to test the backend API and services:

### Running All Tests

To run all tests at once:

```bash
cd backend
./run_tests.sh
```

This script will:
1. Create a virtual environment if it doesn't exist
2. Install dependencies if needed
3. Run all test scripts in sequence

### Running Individual Tests

You can also run individual test scripts:

```bash
cd backend
python test_app.py      # Integration test that starts a server and tests API endpoints
python test_services.py # Unit tests for service layer functions
python test_api.py      # API tests using FastAPI's TestClient
```

### Test Types

1. **Integration Test** (`test_app.py`):
   - Starts a server in a separate thread
   - Tests API endpoints by making HTTP requests
   - Displays the results in the console

2. **Service Unit Tests** (`test_services.py`):
   - Tests individual service functions
   - Uses mock database sessions
   - Verifies the structure and content of returned data

3. **API Tests** (`test_api.py`):
   - Uses FastAPI's TestClient to test API endpoints
   - Does not start an actual server
   - Verifies response status codes and content

## Accessing the Application

- Production build: `http://localhost:8000`
- Development frontend: `http://localhost:5173`
- Backend API: `http://localhost:8000/api`
- API Documentation: `http://localhost:8000/api/docs`
- API ReDoc: `http://localhost:8000/api/redoc`

## Troubleshooting

### Common Issues

1. **Port already in use**
   - If port 8000 is already in use, you can specify a different port:
   ```bash
   uvicorn app.main:app --reload --port 8001
   ```

2. **Module not found errors**
   - Ensure you're running the commands from the correct directory
   - Verify that all dependencies are installed

3. **CORS errors in development mode**
   - The backend is configured to allow requests from the frontend development server
   - If you're seeing CORS errors, check that the backend is running and the CORS settings in `backend/app/main.py` include your frontend URL

4. **Virtual environment issues**
   - If you're having trouble with the virtual environment, you can install dependencies globally:
   ```bash
   pip install -r backend/requirements.txt
   ```

5. **Browserslist database errors**
   - If you see errors related to browserslist or caniuse-lite, you can update them manually:
   ```bash
   npm update caniuse-lite browserslist
   ```

6. **Optional dependencies failing to install**
   - Some dependencies like `anthropic` are optional for the MVP
   - If they fail to install, the application will still work with limited functionality

7. **New terminal window doesn't open in development mode**
   - If the script fails to open a new terminal window for the backend server, you can start it manually:
   ```bash
   cd backend
   source venv/bin/activate
   uvicorn app.main:app --reload
   ```

8. **Backend server still running after stopping the script**
   - If you've stopped the frontend server but the backend is still running, you can find and kill the process:
   ```bash
   # Find the process
   ps aux | grep "uvicorn app.main:app"
   
   # Kill the process (replace <PID> with the process ID from the previous command)
   kill <PID>
   ```

9. **Test failures**
   - If tests are failing, check that the backend server is not already running
   - Ensure all dependencies are installed correctly
   - Look for specific error messages in the test output

For additional help, please refer to the project documentation or open an issue on the repository.
