# PharmaSage

PharmaSage is a comprehensive pharmaceutical business intelligence platform that provides real-time insights into global pharmaceutical trade flows, buyer discovery, and contact intelligence.

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Core Features](#core-features)
  - [Market Intelligence Dashboard](#market-intelligence-dashboard)
  - [Buyer Discovery Engine](#buyer-discovery-engine)
  - [Contact Intelligence](#contact-intelligence)
  - [AI-Powered Deep Research](#ai-powered-deep-research)
- [Component Architecture](#component-architecture)
- [Backend Architecture](#backend-architecture)
  - [Data Integration Layer](#data-integration-layer)
  - [Core API Layer](#core-api-layer)
  - [AI Integration Layer](#ai-integration-layer)
  - [Database Strategy](#database-strategy)
- [UI/UX Design Patterns](#uiux-design-patterns)
- [Data Flow](#data-flow)
- [Data Sources](#data-sources)
- [Setup & Installation](#setup--installation)
- [Development](#development)

## Project Overview

PharmaSage is a next-generation pharmaceutical business intelligence platform designed to help pharmaceutical companies discover global market opportunities, identify qualified buyers, and accelerate business development through AI-powered intelligence. The platform aggregates and analyzes global pharmaceutical trade data, company registries, and regulatory databases to provide actionable insights for pharmaceutical businesses.

## Tech Stack

PharmaSage is built with modern web technologies:

### Frontend
- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite
- **Routing**: React Router v6
- **UI Components**: Shadcn UI (based on Radix UI primitives)
- **Styling**: Tailwind CSS
- **Data Fetching**: TanStack React Query
- **Form Handling**: React Hook Form with Zod validation
- **Data Visualization**: Recharts
- **Icons**: Lucide React
- **Date Handling**: date-fns
- **Toast Notifications**: Sonner

### Backend
- **API Framework**: FastAPI (Python)
- **Database**: PostgreSQL with TimescaleDB extension
- **Data Processing**: Apache Airflow for ETL pipelines
- **Storage**: AWS S3 for data lake
- **Caching**: Redis (optional)
- **AI/ML**: 
  - Anthropic Claude API for guidance generation
  - Perplexity API for deep research on potential buyers
- **Authentication**: OAuth 2.0 with JWT
- **Containerization**: Docker
- **Deployment**: AWS ECS/Fargate

## Project Structure

```
PharmaSage/
├── public/                  # Static assets
├── src/                     # Frontend source code
│   ├── components/          # Reusable components
│   │   ├── ui/              # UI component library (Shadcn UI)
│   │   ├── DashboardHeader.tsx
│   │   ├── MarketFilters.tsx
│   │   ├── MetricsGrid.tsx
│   │   ├── TopExportersTable.tsx
│   │   ├── TrendChart.tsx
│   │   └── WorldMapPlaceholder.tsx
│   ├── hooks/               # Custom React hooks
│   │   ├── use-mobile.tsx
│   │   └── use-toast.ts
│   ├── lib/                 # Utility functions
│   │   └── utils.ts
│   ├── pages/               # Application pages
│   │   ├── BuyerDiscovery.tsx
│   │   ├── ContactIntelligence.tsx
│   │   ├── Index.tsx        # Main dashboard
│   │   ├── Landing.tsx      # Landing/marketing page
│   │   └── NotFound.tsx     # 404 page
│   ├── App.tsx              # Main application component with routing
│   ├── App.css              # Global styles
│   ├── index.css            # Global styles
│   ├── main.tsx             # Application entry point
│   └── vite-env.d.ts        # Vite type definitions
├── backend/                 # Backend source code
│   ├── app/                 # FastAPI application
│   │   ├── api/             # API routes
│   │   │   ├── dashboard.py # Market trends endpoints
│   │   │   ├── search.py    # Product/company search endpoints
│   │   │   ├── match.py     # Prospect matching endpoints
│   │   │   ├── contacts.py  # Contact endpoints
│   │   │   ├── export.py    # Data export endpoints
│   │   │   ├── research.py  # Deep research endpoints
│   │   │   └── analytics.py # Usage tracking endpoints
│   │   ├── core/            # Core application code
│   │   │   ├── config.py    # Configuration settings
│   │   │   ├── security.py  # Security utilities
│   │   │   └── logging.py   # Logging configuration
│   │   ├── db/              # Database related code
│   │   │   ├── session.py   # Database session management
│   │   │   ├── base.py      # Base model class
│   │   │   └── init_db.py   # Database initialization
│   │   ├── models/          # SQLAlchemy ORM models
│   │   │   ├── company.py   # Company model
│   │   │   ├── product.py   # Product model
│   │   │   ├── transaction.py # Transaction model
│   │   │   ├── license.py   # License model
│   │   │   └── contact.py   # Contact model
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── services/        # Business logic
│   │   │   ├── matching.py  # Prospect matching service
│   │   │   ├── buyer_research.py # Buyer research service
│   │   │   └── perplexity_client.py # Perplexity API client
│   │   ├── utils/           # Utility functions
│   │   └── main.py          # FastAPI application entry point
│   ├── data_ingestion/      # Data ingestion pipelines
│   │   ├── airflow/         # Airflow DAGs
│   │   └── scripts/         # Data processing scripts
│   └── tests/               # Backend tests
├── alembic/                 # Database migrations
├── docker/                  # Docker configuration
│   ├── Dockerfile           # Dockerfile for the application
│   └── docker-compose.yml   # Docker Compose configuration
├── .gitignore
├── bun.lockb                # Bun lockfile
├── components.json          # Shadcn UI configuration
├── eslint.config.js         # ESLint configuration
├── index.html               # HTML entry point
├── package-lock.json
├── package.json             # Project dependencies and scripts
├── postcss.config.js        # PostCSS configuration
├── tailwind.config.ts       # Tailwind CSS configuration
├── tsconfig.app.json        # TypeScript configuration
├── tsconfig.json            # TypeScript configuration
├── tsconfig.node.json       # TypeScript configuration for Node
└── vite.config.ts           # Vite configuration
```

## Core Features

### Market Intelligence Dashboard

The Market Intelligence Dashboard provides real-time insights into global pharmaceutical trade flows, emerging trends, and market opportunities.

**Key Components:**
- **MetricsGrid**: Displays key metrics including global trade volume, active products, export companies, and active markets
- **WorldMapPlaceholder**: Visualization of global trade flows with regional indicators
- **TrendChart**: Bar chart visualization of market trends over time
- **TopExportersTable**: Table of top global pharmaceutical exporters with detailed information

**Functionality:**
- Filter data by product type, region, and time period
- View global trade flows on an interactive map
- Analyze market trends and growth rates
- Explore top exporters and their market share

### Buyer Discovery Engine

The Buyer Discovery Engine is an AI-powered prospect identification tool that finds the most relevant buyers for pharmaceutical products.

**Key Components:**
- Search and filtering system for buyers
- Detailed buyer profiles with opportunity scores
- Stats cards showing total buyers, hot leads, active prospects, and markets

**Functionality:**
- Search buyers by name, location, segment
- Filter by market segment, company size, region, and opportunity score
- View detailed buyer information including revenue, purchasing volume, and key products
- Assess opportunity scores and match percentages

### Contact Intelligence

Contact Intelligence provides automated discovery of key decision-makers and stakeholders within target pharmaceutical companies.

**Key Components:**
- Contact directory with detailed profiles
- Search and filtering system for contacts
- Stats cards showing total contacts, key contacts, recent interactions, and companies

**Functionality:**
- Search contacts by name, company, title
- Filter by department, seniority level, relationship score, and last contact
- View detailed contact information including email, phone, department, and interactions
- Track relationship scores and recent activities

### AI-Powered Deep Research

The AI-Powered Deep Research feature uses the Perplexity API to conduct in-depth research on potential buyers for pharmaceutical products.

**Key Components:**
- Perplexity API integration for deep research
- Research-based prospect identification
- Customized outreach guidance for research-based prospects

**Functionality:**
- Conduct deep research on company websites to identify potential buyers
- Generate structured data from research results
- Enhance prospect matching with research-based insights
- Provide customized outreach guidance for research-based prospects
- Cache research results to reduce API calls

## Component Architecture

PharmaSage follows a component-based architecture with:

1. **Page Components**: Located in `src/pages/`, these components represent full pages in the application and are connected to routes in `App.tsx`.

2. **Feature Components**: Located in `src/components/`, these are complex components specific to PharmaSage features, such as `MetricsGrid`, `TopExportersTable`, etc.

3. **UI Components**: Located in `src/components/ui/`, these are reusable UI components from the Shadcn UI library, built on top of Radix UI primitives.

4. **Custom Hooks**: Located in `src/hooks/`, these provide reusable logic for components.

5. **Utility Functions**: Located in `src/lib/`, these provide helper functions for the application.

The application uses React Router for navigation between pages, with routes defined in `App.tsx`.

## Backend Architecture

PharmaSage uses an integrated deployment approach for the MVP, where the FastAPI backend serves the React frontend directly. This simplifies deployment and development while maintaining a clear separation of concerns.

### Data Integration Layer

The data integration layer is responsible for collecting, processing, and storing data from various sources:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Raw Data Lake  │────▶│ Data Processing │────▶│ Structured Data │
│  (S3 Buckets)   │     │  (ETL Pipeline) │     │  (PostgreSQL)   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

1. **Raw Data Lake (S3)**
   - Store raw data from all sources in their original format
   - Organize by source, data type, and ingestion date
   - Implement lifecycle policies for cost optimization

2. **ETL Pipeline (Apache Airflow)**
   - Create DAGs for each data source with appropriate schedules
   - Implement data validation, cleaning, and transformation
   - Handle entity resolution across different sources (e.g., matching company names)

3. **Structured Database (PostgreSQL)**
   - Optimized schema for application queries
   - Partitioning for large tables (transactions, contacts)
   - Materialized views for common dashboard queries

### Core API Layer

The core API layer provides endpoints for the frontend to interact with the backend:

```
┌───────────────────────────────────────────────────────────────────────┐
│                         FastAPI Application                           │
├───────────┬───────────┬───────────┬───────────┬───────────┬───────────┤
│ Dashboard │  Search   │  Matching │  Export   │ Analytics │ Research  │
│   API     │    API    │    API    │    API    │    API    │    API    │
└───────────┴───────────┴───────────┴───────────┴───────────┴───────────┘
```

Key components:

1. **Dashboard API**
   - Endpoints for market trends, top exporters, regional analysis
   - Support for filtering by product type, geography, time period
   - Aggregation logic for visualization data

2. **Search API**
   - Product and company search with autocomplete
   - Fuzzy matching for names and synonyms
   - Filtering by various attributes

3. **Matching API**
   - Core prospect discovery engine
   - Algorithm to match input companies/products with potential buyers
   - Scoring and ranking logic
   - Integration with deep research results

4. **Export API**
   - CSV generation for search results and matches
   - Background processing for large exports
   - Secure download links

5. **Analytics API**
   - Event tracking for user actions
   - Usage metrics collection
   - Feature popularity analysis

6. **Research API**
   - Deep research on potential buyers
   - Integration with Perplexity API
   - Structured data extraction from research results

### AI Integration Layer

The AI integration layer connects to Anthropic's Claude API and Perplexity API for generating guidance and insights:

```
┌───────────────────┐     ┌───────────────────┐
│  Business Logic   │────▶│  AI Orchestrator  │
│     Services      │◀────│     Service       │
└───────────────────┘     └─────────┬─────────┘
                                   │
                                   ▼
                          ┌───────────────────┐
                          │  Anthropic Claude │
                          │       API         │
                          └───────────────────┘
                                   │
                                   ▼
                          ┌───────────────────┐
                          │  Perplexity API   │
                          │                   │
                          └───────────────────┘
```

Components:

1. **AI Orchestrator Service**
   - Manage API calls to Anthropic and Perplexity
   - Handle prompt engineering and context management
   - Implement caching for similar queries
   - Process and format AI responses

2. **AI Use Cases**
   - Generate outreach suggestions based on prospect profiles
   - Provide market entry strategy recommendations
   - Summarize company and product information
   - Create talking points for sales conversations
   - Conduct deep research on potential buyers

### Database Strategy

Given the expected data volume, the database strategy includes:

1. **PostgreSQL for structured data**
   - Appropriate indexing for performance
   - Partitioning for large tables
   - Connection pooling with pgBouncer

2. **TimescaleDB extension for time-series data**
   - Efficient storage and querying of market trends
   - Automatic partitioning by time

3. **Read replicas for analytics queries**
   - Separate read-heavy analytics queries from transactional workloads
   - Scale read capacity independently

## UI/UX Design Patterns

PharmaSage employs several consistent UI/UX design patterns:

1. **Card-Based Layout**: Information is organized in cards with consistent styling.

2. **Consistent Header**: Each page has a header with a title and action buttons.

3. **Stats Cards**: Key metrics are displayed in a grid of stats cards.

4. **Filters**: Data can be filtered using consistent filter components.

5. **Color Coding**: Status and trends are color-coded (e.g., success in green, warnings in amber, errors in red).

6. **Responsive Design**: The UI adapts to different screen sizes using Tailwind's responsive classes.

7. **Gradient Backgrounds**: Subtle gradients are used for visual appeal.

8. **Consistent Icons**: Lucide React icons are used throughout the application.

## Data Flow

The data flow in PharmaSage follows this pattern:

1. **Data Ingestion**:
   - External data sources → Raw Data Lake (S3)
   - ETL pipelines process and transform data
   - Structured data stored in PostgreSQL

2. **API Layer**:
   - FastAPI endpoints query the database
   - Business logic applied in service layer
   - Results returned to frontend

3. **Frontend**:
   - React Query manages API requests and caching
   - Component state handles UI interactions
   - Data visualization components render insights

4. **AI Integration**:
   - User actions trigger AI guidance requests
   - AI Orchestrator sends prompts to Anthropic Claude or Perplexity
   - Responses processed and displayed to users

## Data Sources

PharmaSage integrates with multiple pharmaceutical market intelligence datasets. For the MVP, we'll prioritize:

### UN Comtrade Database
- **Purpose**: Global pharmaceutical trade statistics
- **Data Model**:
  ```json
  {
    "reporter_country": "string",
    "partner_country": "string", 
    "commodity_code": "string (HS 30 - Pharmaceutical products)",
    "trade_flow": "string (Import/Export)",
    "value_usd": "number",
    "quantity_kg": "number",
    "period": "string (YYYY or YYYYMM)",
    "customs_proc_code": "string",
    "mode_of_transport": "string"
  }
  ```
- **Access**: REST API available at comtradeplus.un.org

Additional data sources will be integrated in future phases.

## Setup & Installation

To set up the PharmaSage project locally:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd PharmaSage
   ```

2. **Install frontend dependencies**:
   ```bash
   npm install
   ```

3. **Set up backend**:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   # Make sure to add your Perplexity API key for deep research
   ```

5. **Start the development servers**:
   ```bash
   # Terminal 1 - Frontend
   npm run dev
   
   # Terminal 2 - Backend
   cd backend
   uvicorn app.main:app --reload
   ```

6. **Build for production**:
   ```bash
   npm run build
   ```

7. **Run with Docker**:
   ```bash
   docker-compose up -d
   ```

## Development

The project includes several development tools and configurations:

- **ESLint**: For code linting (`eslint.config.js`)
- **TypeScript**: For type checking (`tsconfig.json`, `tsconfig.app.json`, `tsconfig.node.json`)
- **Tailwind CSS**: For styling (`tailwind.config.ts`, `postcss.config.js`)
- **Vite**: For fast development and building (`vite.config.ts`)
- **FastAPI**: For API development with automatic OpenAPI documentation
- **Alembic**: For database migrations
- **Docker**: For containerized development and deployment

To run linting:
```bash
npm run lint
```

To build for development:
```bash
npm run build:dev
```

To run backend tests:
```bash
cd backend
pytest
```

---

PharmaSage is designed to be a comprehensive solution for pharmaceutical business intelligence, providing valuable insights for market analysis, buyer discovery, and contact management.
