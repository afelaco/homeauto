# -----------------------------
# Login to Azure with an admin account
# -----------------------------
CURR_AZ_USER=$(az account show --query "{user:user.name}" -o tsv)
if [ "$CURR_AZ_USER" != "$AZ_USER" ]; then
    echo "  ➡️ Logging in to Azure CLI..."
    az login

    CURR_AZ_USER=$(az account show --query "{user:user.name}" -o tsv)
    if [ "$CURR_AZ_USER" != "$AZ_USER" ]; then
        echo "  ❌ Login failed or incorrect account. Please try again."
        exit 1
    fi

    echo "  ✅  Azure CLI login complete!"
else
    echo "  ⚠️ Already logged in to Azure CLI!"
fi

# -----------------------------
# Create Terraform Service Principal with Owner role and export credentials
# -----------------------------
CURRENT_AF_SP_NAME=$(az ad sp list --display-name "$AF_SP_NAME" --query '[0].appId' -o tsv)
if [ -n "$CURRENT_AF_SP_NAME" ]; then
    echo "  ⚠️ Service Principal '$AF_SP_NAME' already exists. Resetting credentials..."
    AZ_CREDENTIAL=$(az ad sp credential reset --id "$CURRENT_AF_SP_NAME")
else
    echo "  ➡️ Creating Azure Service Principal $AF_SP_NAME..."
    AZ_CREDENTIAL=$(az ad sp create-for-rbac \
        --name "$AF_SP_NAME" \
        --role Owner \
        --scopes "/subscriptions/$AZ_SUBSCRIPTION_ID")
    echo "  ✅  Azure Service Principal $AF_SP_NAME created!"
fi

# -----------------------------
# Export Service Principal credentials as environment variables
# -----------------------------
AZ_TENANT_ID=$(echo "$AZ_CREDENTIAL" | jq -r .tenant)
AF_CLIENT_ID=$(echo "$AZ_CREDENTIAL" | jq -r .appId)
AF_CLIENT_SECRET=$(echo "$AZ_CREDENTIAL" | jq -r .password)
AF_OBJECT_ID=$(az ad sp list --display-name "$AF_SP_NAME" --query "[].id" -o tsv)

export AZ_TENANT_ID AF_CLIENT_ID AF_CLIENT_SECRET AF_OBJECT_ID

echo "  ✅  Service Principal credentials exported!"

# -----------------------------
# Write Service Principal credentials to config/.env.terraform-sp
# -----------------------------
cat >"$AF_SP_CONFIG" <<EOF
AZURE_CLIENT_ID=$AF_CLIENT_ID
AZURE_CLIENT_SECRET=$AF_CLIENT_SECRET
EOF

echo "  📁 Credentials written to $AF_SP_CONFIG"
