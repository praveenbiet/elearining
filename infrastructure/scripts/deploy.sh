#!/bin/bash

# Exit on error
set -e

# Load environment variables
source .env

# Build and push Docker images
echo "Building and pushing Docker images..."
docker-compose build
docker-compose push

# Apply Kubernetes manifests
echo "Applying Kubernetes manifests..."
kubectl apply -k infrastructure/kubernetes/base

# Wait for deployments to be ready
echo "Waiting for deployments to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/elearning-monolith
kubectl wait --for=condition=available --timeout=300s deployment/elearning-web
kubectl wait --for=condition=available --timeout=300s deployment/elearning-admin

# Run database migrations
echo "Running database migrations..."
kubectl exec -it deployment/elearning-monolith -- alembic upgrade head

echo "Deployment completed successfully!" 