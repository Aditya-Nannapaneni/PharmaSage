# PharmaSage

PharmaSage is a comprehensive pharmaceutical business intelligence platform that provides real-time insights into global pharmaceutical trade flows, buyer discovery, contact intelligence, and compliance monitoring.

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Core Features](#core-features)
  - [Market Intelligence Dashboard](#market-intelligence-dashboard)
  - [Buyer Discovery Engine](#buyer-discovery-engine)
  - [Contact Intelligence](#contact-intelligence)
  - [Compliance Monitoring](#compliance-monitoring)
- [Component Architecture](#component-architecture)
- [UI/UX Design Patterns](#uiux-design-patterns)
- [Data Flow](#data-flow)
- [Setup & Installation](#setup--installation)
- [Development](#development)

## Project Overview

PharmaSage is a next-generation pharmaceutical business intelligence platform designed to help pharmaceutical companies discover global market opportunities, identify qualified buyers, and accelerate business development through AI-powered intelligence. The platform aggregates and analyzes global pharmaceutical trade data, company registries, and regulatory databases to provide actionable insights for pharmaceutical businesses.

## Tech Stack

PharmaSage is built with modern web technologies:

- **Frontend Framework**: React 18 with TypeScript
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

## Project Structure

```
PharmaSage/
├── public/                  # Static assets
├── src/
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
│   │   ├── ComplianceMonitoring.tsx
│   │   ├── ContactIntelligence.tsx
│   │   ├── Index.tsx        # Main dashboard
│   │   ├── Landing.tsx      # Landing/marketing page
│   │   └── NotFound.tsx     # 404 page
│   ├── App.tsx              # Main application component with routing
│   ├── App.css              # Global styles
│   ├── index.css            # Global styles
│   ├── main.tsx             # Application entry point
│   └── vite-env.d.ts        # Vite type definitions
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

### Compliance Monitoring

Compliance Monitoring tracks regulatory status, licensing requirements, and compliance indicators across global markets.

**Key Components:**
- Compliance status dashboard for different regulations
- Recent alerts for compliance issues
- Compliance score trends and upcoming reviews

**Functionality:**
- Monitor compliance status for various regulations
- Track compliance scores and progress
- Receive alerts for compliance issues
- View upcoming regulatory reviews

## Component Architecture

PharmaSage follows a component-based architecture with:

1. **Page Components**: Located in `src/pages/`, these components represent full pages in the application and are connected to routes in `App.tsx`.

2. **Feature Components**: Located in `src/components/`, these are complex components specific to PharmaSage features, such as `MetricsGrid`, `TopExportersTable`, etc.

3. **UI Components**: Located in `src/components/ui/`, these are reusable UI components from the Shadcn UI library, built on top of Radix UI primitives.

4. **Custom Hooks**: Located in `src/hooks/`, these provide reusable logic for components.

5. **Utility Functions**: Located in `src/lib/`, these provide helper functions for the application.

The application uses React Router for navigation between pages, with routes defined in `App.tsx`.

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

Currently, PharmaSage uses mock data for demonstration purposes, but it's structured to work with real data:

1. **Data Fetching**: The application is set up with React Query for data fetching, suggesting an API-driven architecture.

2. **Component State**: Each component manages its own state for UI interactions.

3. **Mock Data**: Mock data is defined within component files for demonstration.

In a production environment, the data flow would likely involve:
- API calls to backend services
- Data transformation and normalization
- Caching with React Query
- State management for complex interactions

## Setup & Installation

To set up the PharmaSage project locally:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd PharmaSage
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm run dev
   ```

4. **Build for production**:
   ```bash
   npm run build
   ```

5. **Preview the production build**:
   ```bash
   npm run preview
   ```

## Development

The project includes several development tools and configurations:

- **ESLint**: For code linting (`eslint.config.js`)
- **TypeScript**: For type checking (`tsconfig.json`, `tsconfig.app.json`, `tsconfig.node.json`)
- **Tailwind CSS**: For styling (`tailwind.config.ts`, `postcss.config.js`)
- **Vite**: For fast development and building (`vite.config.ts`)

To run linting:
```bash
npm run lint
```

To build for development:
```bash
npm run build:dev
```

---

PharmaSage is designed to be a comprehensive solution for pharmaceutical business intelligence, providing valuable insights for market analysis, buyer discovery, contact management, and compliance monitoring.
