# -----------------------------
# Login to Azure with an admin account
# -----------------------------
AZ_CURRENT_ACCOUNT=$(az account show --query "{user:user.name}" -o tsv)
if [ "$AZ_CURRENT_ACCOUNT" != "$AZ_ADMIN_ACCOUNT" ]; then
    echo "  ➡️ Logging in to Azure CLI..."
    az login

    AZ_CURRENT_ACCOUNT=$(az account show --query "{user:user.name}" -o tsv)
    if [ "$AZ_CURRENT_ACCOUNT" != "$AZ_ADMIN_ACCOUNT" ]; then
        echo "  ❌ Login failed or incorrect account. Please try again."
        exit 1
    fi

    echo "  ✅  Azure CLI login complete!"
else
    echo "  ⚠️ Already logged in to Azure CLI!"
fi

# -----------------------------
# Create the Service Principal with Storage Blob Data Contributor role and export credentials
# -----------------------------
EXISTING_SP=$(az ad sp list --display-name "$AZ_SP_NAME" --query '[0].appId' -o tsv)
if [ -n "$EXISTING_SP" ]; then
    echo "  ℹ️ Service Principal '$AZ_SP_NAME' already exists. Resetting credentials..."
    AZ_CREDENTIALS=$(az ad sp credential reset --id "$EXISTING_SP")
else
    echo "  ➡️ Creating Azure Service Principal $AZ_SP_NAME..."
    AZ_CREDENTIALS=$(az ad sp create-for-rbac \
        --name "$AZ_SP_NAME" \
        --role "Storage Blob Data Contributor" \
        --scopes "/subscriptions/$AZ_SUBSCRIPTION_ID")
    echo "  ✅  Azure Service Principal $AZ_SP_NAME created!"
fi

export AZ_TENANT_ID=$(echo "$AZ_CREDENTIALS" | jq -r .tenant)
export AZ_CLIENT_ID=$(echo "$AZ_CREDENTIALS" | jq -r .appId)
export AZ_CLIENT_SECRET=$(echo "$AZ_CREDENTIALS" | jq -r .password)

echo "  ✅  Service Principal credentials exported!"

cat >docker/.env <<EOF
AZURE_TENANT_ID=$AZ_TENANT_ID
AZURE_CLIENT_ID=$AZ_CLIENT_ID
AZURE_CLIENT_SECRET=$AZ_CLIENT_SECRET
EOF

echo "  📁 Credentials written to docker/.env!"
