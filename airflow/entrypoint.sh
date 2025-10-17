#!/usr/bin/env bash
set -e

# Variables
ACCOUNT_NAME="homeautopypi"
CONTAINER_NAME="pypi"

# Login
echo "Logging into Azure..."

az login --service-principal \
    --tenant $AZURE_TENANT_ID \
    --username $AZURE_CLIENT_ID \
    --password $AZURE_CLIENT_SECRET \
    --output none

echo "Login successful."

# Generate SAS token
echo "Generating SAS token for Azure Blob Storage..."

SAS_TOKEN=$(az storage container generate-sas \
    --account-name "$ACCOUNT_NAME" \
    --account-key "$AZURE_STORAGE_KEY" \
    --name "$CONTAINER_NAME" \
    --permissions r \
    --expiry 2025-10-19 \
    --output tsv)

echo "SAS token generated."

# Install wheel from private PyPI
echo "Installing wheel from private PyPI..."

PYPI_URL="https://${ACCOUNT_NAME}.blob.core.windows.net/${CONTAINER_NAME}?${SAS_TOKEN}"
pip install --index-url "$PYPI_URL/simple" airflow

echo "Wheel installed successfully."
