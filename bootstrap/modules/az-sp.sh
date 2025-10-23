# -----------------------------
# Create Azure Service Principal for Terraform
# -----------------------------
echo "  ➡️ Creating Azure Service Principal $AZ_SP_TF_NAME..."
AZ_SP_TF_CREDENTIALS=$(az ad sp create-for-rbac \
    --name "$AZ_SP_TF_NAME" \
    --role Owner \
    --scopes "/subscriptions/$AZ_SUBSCRIPTION_ID" \
    --sdk-auth)
echo "  ✅  Azure Service Principal $AZ_SP_TF_NAME created!"
gh secret set AZ_SP_TF_CREDENTIALS --repo "$GH_REPO" --body "$AZ_SP_TF_CREDENTIALS"
echo "  ✅  Service Principal credentials set in GitHub Actions!"

# -----------------------------
# Assign Cloud Application Administrator role to Service Principal
# -----------------------------
AZ_SP_TF_OBJECT_ID=$(az ad sp list --display-name "$AZ_SP_TF_NAME" --query "[].id" -o tsv)
ROLE_NAME="Cloud Application Administrator"
echo "  ➡️ Assigning $ROLE_NAME role to Service Principal $AZ_SP_TF_NAME..."
ROLE_TEMPLATE_ID=$(az rest \
    --method GET \
    --url "https://graph.microsoft.com/v1.0/directoryRoles" \
    --query "value[?displayName=='$ROLE_NAME'].id" \
    -o tsv)
az rest \
    --method POST \
    --url "https://graph.microsoft.com/v1.0/directoryRoles/$ROLE_TEMPLATE_ID/members/\$ref" \
    --body "{\"@odata.id\": \"https://graph.microsoft.com/v1.0/directoryObjects/$AZ_SP_TF_OBJECT_ID\"}"
echo "  ✅ Successfully assigned $ROLE_NAME role to Service Principal $AZ_SP_TF_NAME"
