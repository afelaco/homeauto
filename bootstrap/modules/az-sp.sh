# -----------------------------
# Create Terraform Service Principal with Owner role and export credentials
# -----------------------------
echo "  ➡️ Creating Azure Service Principal $AZ_SP_TF_NAME..."
AZ_SP_TF_CREDENTIALS=$(az ad sp create-for-rbac \
    --name "$AZ_SP_TF_NAME" \
    --role Owner \
    --scopes "/subscriptions/$AZ_SUBSCRIPTION_ID" \
    --sdk-auth)
echo "  ✅  Azure Service Principal $AZ_SP_TF_NAME created!"

# -----------------------------
# Export Service Principal credentials as environment variables
# -----------------------------
export AZ_SP_TF_CREDENTIALS
echo "  ✅  Service Principal credentials exported!"
