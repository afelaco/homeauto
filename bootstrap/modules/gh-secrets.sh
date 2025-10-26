# -----------------------------
# Set GitHub Actions secrets
# -----------------------------
echo "  ➡️ Uploading secrets to GitHub Actions..."
secrets=(
    AZ_SUBSCRIPTION_ID
    GH_TOKEN
    GL_TOKEN
)
for secret in "${secrets[@]}"; do
    if [ -z "${!secret}" ]; then
        echo "    ⚠️ Warning: $secret is empty or not set."
    fi
    gh secret set "$secret" --repo "$GH_REPO" --body "${!secret}"
done

# -----------------------------
# Set Key Vault secrets in GitHub Actions
# -----------------------------
echo "  ➡️ Uploading Key Vault secrets to GitHub Actions..."
gh secret set "AZ_KV_SECRETS" --repo "$GH_REPO" --body "$(cat "$AZ_KV_SECRETS_FILE")"
echo "    ✅ Key Vault secrets uploaded!"
