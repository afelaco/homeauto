#!/usr/bin/env bash
set -euo pipefail

# -----------------------------
# Set current working directory
# -----------------------------
cd "$(git rev-parse --show-toplevel)"

# -----------------------------
# Load configuration
# -----------------------------
source vars/.env.dev
source vars/.env.prd

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
# Create/update Azure Service Principals
# -----------------------------
echo "➡️ Creating Azure Service Principal..."
#source bootstrap/modules/az-login.sh
#source bootstrap/modules/az-sp.sh
echo "✅ Azure bootstrap complete!"

# -----------------------------
# Terraform bootstrap: create backend if not exists
# -----------------------------
echo "➡️ Running Terraform bootstrap..."
if [ ! -f "$TF_BE_CONFIG_FILE" ]; then
    source "modules/tf-backend.sh"
    echo "✅ Terraform bootstrap complete!"
else
    echo "⚠️ Terraform backend configuration already exists at $TF_BE_CONFIG_FILE!"
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
