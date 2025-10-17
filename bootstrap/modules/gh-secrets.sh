# -----------------------------
# Authenticate GitHub CLI using token
# -----------------------------
echo "$GH_TOKEN" | gh auth login --with-token

# -----------------------------
# Set the Azure Service Principal credentials as a GitHub Actions secret
# -----------------------------
echo "  ➡️ Uploading Azure Service Principal credentials to GitHub Actions..."

gh secret set AZ_TENANT_ID --repo "$GH_REPO" --body "$AZ_TENANT_ID"
gh secret set AZ_SUBSCRIPTION_ID --repo "$GH_REPO" --body "$AZ_SUBSCRIPTION_ID"
gh secret set TF_CLIENT_ID --repo "$GH_REPO" --body "$TF_CLIENT_ID"
gh secret set TF_CLIENT_SECRET --repo "$GH_REPO" --body "$TF_CLIENT_SECRET"
gh secret set TF_OBJECT_ID --repo "$GH_REPO" --body "$TF_OBJECT_ID"
gh secret set AF_CLIENT_ID --repo "$GH_REPO" --body "$AF_CLIENT_ID"
gh secret set AF_CLIENT_SECRET --repo "$GH_REPO" --body "$AF_CLIENT_SECRET"

# -----------------------------
# Set Docker Hub credentials as a GitHub Actions secret
# -----------------------------
echo "  ➡️ Uploading Docker Hub credentials to GitHub Actions..."

gh secret set DH_USER --repo "$GH_REPO" --body "$DH_USER"
gh secret set DH_PASSWORD --repo "$GH_REPO" --body "$DH_PASSWORD"

# -----------------------------
# Set PyPI as a GitHub Actions secret
# -----------------------------
echo "  ➡️ Uploading Docker Hub credentials to GitHub Actions..."

gh secret set PYPI_SA --repo "$GH_REPO" --body "$PYPI_SA"
gh secret set PYPI_CONTAINER --repo "$GH_REPO" --body "$PYPI_CONTAINER"

# -----------------------------
# Set the Key Vault secrets as GitHub Actions secrets
# -----------------------------
#echo "  ➡️ Uploading '$GH_SECRETS_FILE' to GitHub Actions..."
#
#for key in $(jq -r 'keys[]' "$GH_SECRETS_FILE"); do
#    value=$(jq -r --arg k "$key" '.[$k]' "$GH_SECRETS_FILE")
#    secret_name="TF_VAR_$(echo "$key" | tr '[:lower:]' '[:upper:]')"
#    gh secret set "$secret_name" \
#        --repo "$GH_REPO" \
#        --body "$value"
#done
#
#echo "  ✅ GitHub Actions secrets upload complete!"
