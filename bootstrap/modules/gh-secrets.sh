# -----------------------------
# Authenticate GitHub CLI using token
# -----------------------------
echo "$GH_TOKEN" | gh auth login --with-token

# -----------------------------
# Set GitHub Actions secrets
# -----------------------------
echo "  ➡️ Uploading secrets to GitHub Actions..."

secrets=(
    AZ_SUBSCRIPTION_ID
    AZ_SP_TF_CREDENTIALS
    DH_USERNAME
    DH_PASSWORD
    GH_TOKEN
)

for secret in "${secrets[@]}"; do
    if [ -z "${!secret}" ]; then
        echo "    ⚠️ Warning: $secret is empty or not set."
    fi
    gh secret set "$secret" --repo "$GH_REPO" --body "${!secret}"
done

# -----------------------------
# Set external secrets in GitHub Actions
# -----------------------------
echo "  ➡️ Uploading Key Vault secrets to GitHub Actions..."
VAR=$(cat "$AZ_KV_SECRETS_FILE")
echo "$VAR"

gh secret set "AZ_KV_SECRETS" --repo "$GH_REPO" --body "$(cat "$AZ_KV_SECRETS_FILE")"
echo "    ✅ Key Vault secrets uploaded!"
