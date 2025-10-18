# -----------------------------
# Authenticate GitHub CLI using token
# -----------------------------
echo "$GH_TOKEN" | gh auth login --with-token

# -----------------------------
# Set the Azure Service Principal credentials as a GitHub Actions secret
# -----------------------------
echo "  ➡️ Uploading Azure Service Principal credentials to GitHub Actions..."

for var in $(printenv | grep -E '^(AZ_|TF_)' | cut -d= -f1); do
    if [ -z "${!var}" ]; then
        echo "    ⚠️ $var is empty or not set!"
    fi
    gh secret set "$var" --repo "$GH_REPO" --body "${!var}"
done
