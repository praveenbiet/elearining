#!/bin/bash

# Create main directories
mkdir -p monolith/src/{api,common,modules,schemas,tasks,cli,db/migrations,tests/{unit,integration,performance},static}
mkdir -p apps/{web-app,admin-portal}/src/{app,features,shared,entities,styles,assets,i18n,tests}
mkdir -p shared/{backend-python/platform_shared,frontend-libs/{design-system,common-hooks,api-client}}
mkdir -p infrastructure/{environments/{production,staging},modules}
mkdir -p docs/{architecture,api-reference,guides,adrs}
mkdir -p scripts
mkdir -p config/{production,staging}
mkdir -p helm/elearning-platform/{templates,charts}

# Create initial files
touch monolith/src/__init__.py
touch monolith/src/main.py
touch monolith/requirements.txt
touch monolith/Dockerfile
touch monolith/pytest.ini

# Create frontend package.json files
touch apps/web-app/package.json
touch apps/admin-portal/package.json

# Create shared library files
touch shared/backend-python/pyproject.toml
touch shared/backend-python/requirements.txt
touch shared/frontend-libs/design-system/package.json

# Create infrastructure files
touch infrastructure/main.tf
touch infrastructure/variables.tf
touch infrastructure/outputs.tf

# Create documentation files
touch docs/architecture/index.md
touch docs/api-reference/index.md
touch docs/guides/index.md
touch docs/adrs/index.md

# Create configuration files
touch config/production/monolith-api.yaml
touch config/staging/monolith-api.yaml

# Create Helm files
touch helm/elearning-platform/Chart.yaml
touch helm/elearning-platform/values.yaml

# Make scripts executable
chmod +x scripts/*.sh

echo "Project structure created successfully!" 