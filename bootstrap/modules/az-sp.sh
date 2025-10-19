# -----------------------------
# Create Terraform Service Principal with Owner role and export credentials
# -----------------------------
AZ_SP_TF_ID=$(az ad sp list --display-name "$AZ_SP_TF_NAME" --query '[0].appId' -o tsv)
if [ -n "$AZ_SP_TF_ID" ]; then
    echo "  ⚠️ Service Principal '$AZ_SP_TF_NAME' already exists. Resetting credentials..."
    AZ_SP_TF_CREDENTIALS=$(az ad sp credential reset \
        --id "$AZ_SP_TF_ID")
else
    echo "  ➡️ Creating Azure Service Principal $AZ_SP_TF_NAME..."
    AZ_SP_TF_CREDENTIALS=$(az ad sp create-for-rbac \
        --name "$AZ_SP_TF_NAME" \
        --role Owner \
        --scopes "/subscriptions/$AZ_SUBSCRIPTION_ID")
    echo "  ✅  Azure Service Principal $AZ_SP_TF_NAME created!"
fi

# -----------------------------
# Export Service Principal credentials as environment variables
# -----------------------------
export AZ_SP_TF_CREDENTIALS
echo "  ✅  Service Principal credentials exported!"
