#!/usr/bin/env bash
set -euo pipefail

# -----------------------------
# Set current working directory
# -----------------------------
cd "$(git rev-parse --show-toplevel)"

# -----------------------------
# Load configuration from .env file
# -----------------------------
source .env

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
# Create Azure Service Principal or refresh its credentials
# -----------------------------
#echo "➡️ Updating Azure Service Principal..."
#source "scripts/bootstrap/modules/az-sp.sh"
#echo "✅ Azure bootstrap complete!"

# -----------------------------
# Set GitHub Actions secrets
# -----------------------------
#echo "➡️ Setting GitHub Actions secrets..."
#source "scripts/bootstrap/modules/gh-secrets.sh"
#echo "✅ GitHub bootstrap complete!"

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
