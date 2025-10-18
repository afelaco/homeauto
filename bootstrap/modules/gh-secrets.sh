# -----------------------------
# Authenticate GitHub CLI using token
# -----------------------------
echo "$GH_TOKEN" | gh auth login --with-token

# -----------------------------
# Set GitHub Actions secrets
# -----------------------------
echo "  ➡️ Uploading secrets to GitHub Actions..."

secrets=(
    # GitHub Actions
    AZ_TENANT_ID
    AZ_SUBSCRIPTION_ID
    AZ_SP_TF_CLIENT_ID
    AZ_SP_TF_CLIENT_SECRET
    AZ_SP_TF_OBJECT_ID
    DH_USERNAME
    DH_PASSWORD
    # Key Vault
    TF_VAR_STEAM_ID
    TF_VAR_STEAM_KEY
)

for secret in "${secrets[@]}"; do
    if [ -z "${!secret}" ]; then
        echo "    ⚠️ Warning: $secret is empty or not set."
    fi
    gh secret set "$secret" --repo "$GH_REPO" --body "${!secret}"
done
