# E-Learning Platform

A modern, scalable e-learning platform built with a modular monolith architecture.

## Project Structure

The project follows a modular monolith architecture with the following main components:

- `monolith/` - Backend monolith application (FastAPI)
- `apps/` - Frontend applications
  - `web-app/` - Main user-facing web application
  - `admin-portal/` - Admin management portal
- `shared/` - Shared libraries and components
  - `backend-python/` - Shared Python utilities
  - `frontend-libs/` - Shared frontend components and utilities
- `infrastructure/` - Infrastructure as Code (Terraform)
- `docs/` - Project documentation
- `scripts/` - Utility scripts
- `config/` - Configuration files
- `helm/` - Kubernetes deployment configurations

## Technology Stack

### Backend
- FastAPI (Python)
- PostgreSQL
- Redis
- Kafka
- Elasticsearch

### Frontend
- React
- TypeScript
- Redux Toolkit
- RTK Query
- Tailwind CSS

### Infrastructure
- Docker
- Kubernetes
- Terraform
- Helm

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 16+
- Docker
- Kubernetes
- Terraform

### Development Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   # Backend
   cd monolith
   pip install -r requirements.txt
   
   # Frontend
   cd apps/web-app
   npm install
   
   cd ../admin-portal
   npm install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   ```

4. Start development servers:
   ```bash
   # Backend
   cd monolith
   uvicorn src.main:app --reload
   
   # Frontend
   cd apps/web-app
   npm run dev
   
   cd ../admin-portal
   npm run dev
   ```

## Documentation

Detailed documentation can be found in the `docs/` directory:
- Architecture overview
- API reference
- Development guides
- Deployment guides
- ADRs (Architecture Decision Records)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 