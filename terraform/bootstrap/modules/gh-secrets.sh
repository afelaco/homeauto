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
gh secret set AZURE_OBJECT_ID --repo "$GH_REPO" --body "$AZ_OBJECT_ID"

# -----------------------------
# Set the Key Vault secrets as GitHub Actions secrets
# -----------------------------
echo "  ➡️ Uploading '$GH_SECRETS_FILE' to GitHub Actions..."

for key in $(jq -r 'keys[]' "$GH_SECRETS_FILE"); do
  value=$(jq -r --arg k "$key" '.[$k]' "$GH_SECRETS_FILE")
  secret_name="TF_VAR_$(echo "$key" | tr '[:lower:]' '[:upper:]')"
  gh secret set "$secret_name" \
    --repo "$GH_REPO"\
    --body "$value"
done

echo "  ✅ GitHub Actions secrets upload complete!"
