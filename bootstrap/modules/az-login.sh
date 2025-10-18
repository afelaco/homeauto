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
