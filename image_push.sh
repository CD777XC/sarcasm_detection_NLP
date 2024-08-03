#!/bin/bash

# Load variables from .env file
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
else
    echo ".env file not found. Please create a .env file with the necessary variables."
    exit 1
fi

# Build the Docker image
echo "Building the Docker image... 🚀"
docker build -t eu.gcr.io/$GCP_PROJECT_ID/$DOCKER_IMAGE_NAME .
if [ $? -ne 0 ]; then
    echo "Docker build failed ❌"
    exit 1
fi

# Push the Docker image to Google Container Registry
echo "Pushing the Docker image to Google Container Registry... 📨"
docker push eu.gcr.io/$GCP_PROJECT_ID/$DOCKER_IMAGE_NAME
if [ $? -ne 0 ]; then
    echo "Docker push failed ❌"
    exit 1
fi

# Deploy the image to Google Cloud Run
echo "Deploying the image to Google Cloud Run... 🌐"
gcloud run deploy --image eu.gcr.io/$GCP_PROJECT_ID/$DOCKER_IMAGE_NAME --platform managed --region $GCP_REGION
if [ $? -ne 0 ]; then
    echo "gcloud run deploy failed ❌"
    exit 1
fi

echo "Deployment completed successfully ✅"