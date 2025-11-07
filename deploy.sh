#!/bin/bash

# Golf Battle-Buddy Deployment Script for Google Cloud Run
# This script automates the deployment process to Google Cloud Run

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
APP_NAME="golfbb-app"
REGION="us-central1"
PORT="8080"

echo -e "${GREEN}=== Golf Battle-Buddy Deployment Script ===${NC}\n"

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo -e "${RED}Error: gcloud CLI is not installed${NC}"
    echo "Please install it from: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

# Get current project
PROJECT_ID=$(gcloud config get-value project 2>/dev/null)

if [ -z "$PROJECT_ID" ]; then
    echo -e "${RED}Error: No Google Cloud project is set${NC}"
    echo "Please run: gcloud config set project YOUR_PROJECT_ID"
    exit 1
fi

echo -e "${GREEN}Current project:${NC} $PROJECT_ID"
echo -e "${GREEN}App name:${NC} $APP_NAME"
echo -e "${GREEN}Region:${NC} $REGION\n"

# Check for --yes flag for automated deployment
SKIP_CONFIRMATION=false
if [[ "$1" == "--yes" ]] || [[ "$1" == "-y" ]]; then
    SKIP_CONFIRMATION=true
    echo -e "${YELLOW}Skipping confirmation (automated mode)${NC}\n"
fi

# Ask for confirmation (unless --yes flag is provided)
if [ "$SKIP_CONFIRMATION" = false ]; then
    read -p "Deploy to Google Cloud Run? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${YELLOW}Deployment cancelled${NC}"
        exit 0
    fi
fi

echo -e "\n${GREEN}Enabling required APIs...${NC}"
gcloud services enable run.googleapis.com || echo "Cloud Run API already enabled"
gcloud services enable cloudbuild.googleapis.com || echo "Cloud Build API already enabled"

echo -e "\n${GREEN}Deploying to Cloud Run...${NC}"
gcloud run deploy $APP_NAME \
    --source . \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --port $PORT

if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}=== Deployment Successful! ===${NC}"
    echo -e "Your application is now available at:"
    gcloud run services describe $APP_NAME --region $REGION --format='value(status.url)'
else
    echo -e "\n${RED}Deployment failed. Please check the error messages above.${NC}"
    exit 1
fi
