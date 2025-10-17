# -----------------------------
# Authenticate GitHub CLI using token
# -----------------------------
echo "$GH_TOKEN" | gh auth login --with-token

# -----------------------------
# Set the Azure Service Principal credentials as a GitHub Actions secret
# -----------------------------
echo "  ➡️ Uploading Azure Service Principal credentials to GitHub Actions..."

gh secret set AZURE_TENANT_ID --repo "$GH_REPO" --body "$AZ_TENANT_ID"
gh secret set AZURE_SUBSCRIPTION_ID --repo "$GH_REPO" --body "$AZ_SUBSCRIPTION_ID"
gh secret set AZURE_CLIENT_ID --repo "$GH_REPO" --body "$AZ_CLIENT_ID"
gh secret set AZURE_CLIENT_SECRET --repo "$GH_REPO" --body "$AZ_CLIENT_SECRET"

# -----------------------------
# Set Docker Hub credentials as a GitHub Actions secret
# -----------------------------
echo "  ➡️ Uploading Docker Hub credentials to GitHub Actions..."

gh secret set DOCKERHUB_USERNAME --repo "$GH_REPO" --body "$DH_USERNAME"
gh secret set DOCKERHUB_PASSWORD --repo "$GH_REPO" --body "$DH_PASSWORD"
