#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to check if a command exists
command_exists() {
  command -v "$1" >/dev/null 2>&1
}

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

# Check for required dependencies
print_status "Checking for required dependencies..."

# Check for Node.js and npm
if ! command_exists node; then
  print_error "Node.js is not installed. Please install Node.js and try again."
  exit 1
else
  NODE_VERSION=$(node -v)
  print_status "Found Node.js $NODE_VERSION"
fi

if ! command_exists npm; then
  print_error "npm is not installed. Please install npm and try again."
  exit 1
else
  NPM_VERSION=$(npm -v)
  print_status "Found npm $NPM_VERSION"
fi

# Check for Python and pip
if ! command_exists python3; then
  print_error "Python 3 is not installed. Please install Python 3 and try again."
  exit 1
else
  PYTHON_VERSION=$(python3 --version)
  print_status "Found $PYTHON_VERSION"
fi

if ! command_exists pip3; then
  print_error "pip3 is not installed. Please install pip3 and try again."
  exit 1
else
  PIP_VERSION=$(pip3 --version | awk '{print $2}')
  print_status "Found pip $PIP_VERSION"
fi

# Update browserslist database
print_status "Updating browserslist database..."
npm update caniuse-lite browserslist || print_warning "Failed to update browserslist database. Continuing anyway."

# Install frontend dependencies
print_status "Installing frontend dependencies..."
print_warning "This may take a few minutes. Please be patient..."
if [ ! -d "node_modules" ]; then
  npm install --no-progress
  if [ $? -ne 0 ]; then
    print_error "Failed to install frontend dependencies."
    exit 1
  fi
  print_status "Frontend dependencies installed successfully."
else
  print_status "Frontend dependencies already installed."
fi

# Install backend dependencies
print_status "Installing backend dependencies..."
cd backend || exit 1
if [ ! -d "venv" ]; then
  print_status "Creating Python virtual environment..."
  python3 -m venv venv
  source venv/bin/activate
  print_warning "Installing Python packages. This may take a few minutes..."
  
  # Install packages with pip, but continue even if some fail
  pip3 install -r requirements.txt || print_warning "Some Python packages could not be installed. The application may still work with limited functionality."
  
  print_status "Backend dependencies installation completed."
else
  print_status "Activating existing virtual environment..."
  source venv/bin/activate
  print_status "Updating backend dependencies..."
  
  # Update packages with pip, but continue even if some fail
  pip3 install -r requirements.txt || print_warning "Some Python packages could not be updated. The application may still work with limited functionality."
fi

# Start backend server in the background
print_status "Starting backend server..."
print_status "The backend API will be available at http://localhost:8000/api"
cd ..

# Try different terminal commands based on the OS
print_status "Opening a new terminal window for the backend server..."
print_warning "If a new terminal doesn't open, you may need to start the backend server manually."

# Create a backend start script
cat > backend_start.sh << 'EOF'
#!/bin/bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload
EOF

chmod +x backend_start.sh

# Try different terminal commands based on the OS
gnome-terminal -- bash -c "./backend_start.sh; exec bash" 2>/dev/null || \
xterm -e "./backend_start.sh" 2>/dev/null || \
osascript -e 'tell app "Terminal" to do script "cd '$PWD' && ./backend_start.sh"' 2>/dev/null || \
start "Backend Server" cmd /k "backend_start.sh" 2>/dev/null || \
print_warning "Could not open a new terminal window. Please open a new terminal and run: cd backend && source venv/bin/activate && uvicorn app.main:app --reload"

# Wait a moment for the backend to start
print_status "Waiting for backend server to start..."
sleep 3

# Start frontend dev server
print_status "Starting frontend development server..."
print_status "The frontend will be available at http://localhost:5173"
print_status "Press Ctrl+C to stop the frontend server."
npm run dev

print_status "Development servers stopped."
