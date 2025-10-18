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
AZ_SP_TF_CLIENT_ID=$(echo "$AZ_CREDENTIAL" | jq -r .appId)
AZ_SP_TF_CLIENT_SECRET=$(echo "$AZ_CREDENTIAL" | jq -r .password)
TF_VAR_AZ_SP_TF_OBJECT_ID=$(az ad sp list --display-name "$TF_SP_NAME" --query "[].id" -o tsv)

export AZ_SP_TF_CLIENT_ID AZ_SP_TF_CLIENT_SECRET TF_VAR_AZ_SP_TF_OBJECT_ID

echo "  ✅  Service Principal credentials exported!"
