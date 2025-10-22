echo "  ➡️ Creating Azure Service Principal $AZ_SP_TF_NAME..."
AZ_SP_TF_CREDENTIALS=$(az ad sp create-for-rbac \
    --name "$AZ_SP_TF_NAME" \
    --role Owner \
    --scopes "/subscriptions/$AZ_SUBSCRIPTION_ID" \
    --sdk-auth)
echo "  ✅  Azure Service Principal $AZ_SP_TF_NAME created!"
gh secret set AZ_SP_TF_CREDENTIALS --repo "$GH_REPO" --body "$AZ_SP_TF_CREDENTIALS"
echo "  ✅  Service Principal credentials set in GitHub Actions!"

echo "  ➡️ Assigning Cloud Application Administrator role to Service Principal $AZ_SP_TF_NAME..."
AZ_SP_TF_OBJECT_ID=$(az ad sp list --display-name "$AZ_SP_TF_NAME" --query "[].id" -o tsv)
az role assignment create \
    --assignee "$AZ_SP_TF_OBJECT_ID" \
    --role "Cloud Application Administrator" \
    --scope "/subscriptions/$AZ_SUBSCRIPTION_ID"
echo "  ✅  'Cloud Application Administrator' role assigned to Service Principal $AZ_SP_TF_NAME!"
