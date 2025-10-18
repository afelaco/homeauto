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
CURRENT_TF_SP_NAME=$(az ad sp list --display-name "$TF_SP_NAME" --query '[0].appId' -o tsv)
if [ -n "$CURRENT_TF_SP_NAME" ]; then
    echo "  ⚠️ Service Principal '$TF_SP_NAME' already exists. Resetting credentials..."
    AZ_CREDENTIAL=$(az ad sp credential reset --id "$CURRENT_TF_SP_NAME")
else
    echo "  ➡️ Creating Azure Service Principal $TF_SP_NAME..."
    AZ_CREDENTIAL=$(az ad sp create-for-rbac \
        --name "$TF_SP_NAME" \
        --role Owner \
        --scopes "/subscriptions/$AZ_SUBSCRIPTION_ID")
    echo "  ✅  Azure Service Principal $TF_SP_NAME created!"
fi

# -----------------------------
# Export Service Principal credentials as environment variables
# -----------------------------
AZ_TENANT_ID=$(echo "$AZ_CREDENTIAL" | jq -r .tenant)
TF_CLIENT_ID=$(echo "$AZ_CREDENTIAL" | jq -r .appId)
TF_CLIENT_SECRET=$(echo "$AZ_CREDENTIAL" | jq -r .password)
TF_OBJECT_ID=$(az ad sp list --display-name "$TF_SP_NAME" --query "[].id" -o tsv)

export AZ_TENANT_ID TF_CLIENT_ID TF_CLIENT_SECRET TF_OBJECT_ID

echo "  ✅  Service Principal credentials exported!"
