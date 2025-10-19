if [ "$(az account show --query "{user:user.name}" -o tsv)" != "$AZ_USER" ]; then
    echo "  ➡️ Logging in to Azure CLI..."
    az login
    echo "  ✅  Azure CLI login complete!"
else
    echo "  ⚠️ Already logged in to Azure CLI!"
fi
