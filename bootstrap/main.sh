#!/usr/bin/env bash
set -euo pipefail

# -----------------------------
# Set current working directory
# -----------------------------
cd "$(git rev-parse --show-toplevel)"

# -----------------------------
# Load configuration
# -----------------------------
source config/.env.shared
source config/.env.secret

# -----------------------------
# Sync system environment with Brewfile
# -----------------------------
echo "➡️ Syncing system environment with Brewfile..."
brew bundle
echo "✅ System environment synced!"

# -----------------------------
# Set repo-level Git identity
# -----------------------------
echo "➡️ Setting repo-level Git identity..."
source bootstrap/modules/git-config.sh
echo "✅ Git bootstrap complete!"

# -----------------------------
# Login to Azure with an admin account
# -----------------------------
CURR_AZ_USER=$(az account show --query "{user:user.name}" -o tsv)
if [ "$CURR_AZ_USER" != "$AZ_USER" ]; then
    echo "  ➡️ Logging in to Azure CLI..."
    az login

    CURR_AZ_USER=$(az account show --query "{user:user.name}" -o tsv)
    if [ "$CURR_AZ_USER" != "$AZ_USER" ]; then
        echo "  ❌ Login failed or incorrect account. Please try again."
        exit 1
    fi

    echo "  ✅  Azure CLI login complete!"
else
    echo "  ⚠️ Already logged in to Azure CLI!"
fi

# -----------------------------
# Create/update Azure Service Principals
# -----------------------------
echo "➡️ Updating Azure Service Principal..."

source bootstrap/modules/az-sp.sh

SP_LIST=(
    "terraform-sp:Owner"
    "airflow-sp:Storage Blob Data Contributor"
)

for entry in "${SP_LIST[@]}"; do
    SP_NAME="${entry%%:*}"
    SP_ROLE="${entry#*:}"
    create_sp "$SP_NAME" "$SP_ROLE"
done

echo "✅ Azure bootstrap complete!"

# -----------------------------
# Terraform bootstrap: create backend if not exists
# -----------------------------
echo "➡️ Running Terraform bootstrap..."
if [ ! -f "$TF_BE_CONFIG" ]; then
    source "modules/tf-backend.sh"
    echo "✅ Terraform bootstrap complete!"
else
    echo "⚠️ Terraform backend configuration already exists at $TF_BE_CONFIG!"
fi

# -----------------------------
# Set GitHub Actions secrets
# -----------------------------
echo "➡️ Setting GitHub Actions secrets..."
source bootstrap/modules/gh-secrets.sh
echo "✅ GitHub bootstrap complete!"

# -----------------------------
# Sync virtual environment
# -----------------------------
echo "➡️ Syncing virtual environment..."
uv sync --all-groups
echo "✅ Virtual environment synced!"

# -----------------------------
# Install pre-commit hooks
# -----------------------------
echo "➡️ Installing pre-commit hooks..."
uv run pre-commit clean
uv run pre-commit install
echo "✅ Pre-commit hooks installed!"

# -----------------------------
# Bootstrap complete
# -----------------------------
echo "✅ Bootstrap complete!"
