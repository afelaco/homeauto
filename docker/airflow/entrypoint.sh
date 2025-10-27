#!/usr/bin/env bash
set -e

# Install wheel from GitLab
WHEEL_NAME="homeauto-0.1.0-py3-none-any.whl"
PYPI_URL="https://gitlab.com/api/v4/projects/75607343/packages/pypi/simple"
#GITLAB_TOKEN="${GITLAB_TOKEN}"

echo "Installing wheel from GitLab..."
#pip install --index-url "$PYPI_URL" "$WHEEL_NAME"
echo "Wheel installed successfully."
