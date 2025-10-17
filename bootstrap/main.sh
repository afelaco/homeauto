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
# Create Azure Service Principal for Terraform or refresh its credentials
# -----------------------------
echo "➡️ Updating Azure Service Principal..."
source bootstrap/modules/az-sp-tf.sh
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
# Create Azure Service Principal for Airflow or refresh its credentials
# -----------------------------
echo "➡️ Updating Azure Service Principal..."
source bootstrap/modules/az-sp-af.sh
echo "✅ Azure bootstrap complete!"

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
uv sync
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
