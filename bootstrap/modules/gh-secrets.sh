# -----------------------------
# Authenticate GitHub CLI using token
# -----------------------------
echo "$GH_TOKEN" | gh auth login --with-token

# -----------------------------
# Set the Azure Service Principal credentials as a GitHub Actions secret
# -----------------------------
echo "  ➡️ Uploading Azure Service Principal credentials to GitHub Actions..."

credentials=(
    AZ_TENANT_ID
    AZ_SUBSCRIPTION_ID
    TF_CLIENT_ID
    TF_CLIENT_SECRET
    TF_OBJECT_ID
    AF_CLIENT_ID
    AF_CLIENT_SECRET
)

for credential in "${credentials[@]}"; do
    if [ -z "${!credential}" ]; then
        echo "    ⚠️ Warning: $credential is empty or not set."
    fi
    gh secret set "$credential" --repo "$GH_REPO" --body "${!credential}"
done

# -----------------------------
# Set .env.secrets as GitHub Actions secrets
# -----------------------------
echo "  ➡️ Uploading .env.secrets to GitHub Actions..."

secrets=(
    DH_USER
    DH_PASSWORD
    STEAM_ID
    STEAM_KEY
)

for secret in "${secrets[@]}"; do
    if [ -z "${!secret}" ]; then
        echo "    ⚠️ Warning: $secret is empty or not set."
    fi
    gh secret set "$secret" --repo "$GH_REPO" --body "${!secret}"
done
