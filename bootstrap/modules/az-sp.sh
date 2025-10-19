echo "  ➡️ Creating Azure Service Principal $AZ_SP_TF_NAME..."
AZ_SP_TF_CREDENTIALS=$(az ad sp create-for-rbac \
    --name "$AZ_SP_TF_NAME" \
    --role Owner \
    --scopes "/subscriptions/$AZ_SUBSCRIPTION_ID")
echo "  ✅  Azure Service Principal $AZ_SP_TF_NAME created!"
gh secret set AZ_SP_TF_CREDENTIALS --repo "$GH_REPO" --body "$AZ_SP_TF_CREDENTIALS"
echo "  ✅  Service Principal credentials set in GitHub Actions!"
