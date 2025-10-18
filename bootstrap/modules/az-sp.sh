create_sp() {
    local SP_NAME="$1"
    local SP_ROLE="$2"

    echo "  ➡️  Creating Service Principal $SP_NAME with role $SP_ROLE)"

    local EXISTING_APP_ID
    EXISTING_APP_ID=$(az ad sp list --display-name "$SP_NAME" --query '[0].appId' -o tsv)

    local AZ_CREDENTIAL
    if [[ -n $EXISTING_APP_ID ]]; then
        echo "  ⚠️  Service Principal '$SP_NAME' already exists. Resetting credentials..."
        AZ_CREDENTIAL=$(az ad sp credential reset --id "$EXISTING_APP_ID")
    else
        echo "  ➡️  Creating Azure Service Principal '$SP_NAME'..."
        AZ_CREDENTIAL=$(az ad sp create-for-rbac \
            --name "$SP_NAME" \
            --role "$SP_ROLE" \
            --scopes "/subscriptions/$AZ_SUBSCRIPTION_ID")
        echo "  ✅  Azure Service Principal '$SP_NAME' created!"
    fi

    # normalize SP_NAME: replace hyphens with underscores and uppercase
    SP_NAME_VAR=$(echo "$SP_NAME" | tr '-' '_' | tr '[:lower:]' '[:upper:]')

    declare -x "AZ_${SP_NAME_VAR}_CLIENT_ID=$(echo "$AZ_CREDENTIAL" | jq -r .appId)"
    declare -x "AZ_${SP_NAME_VAR}_CLIENT_SECRET=$(echo "$AZ_CREDENTIAL" | jq -r .password)"
    declare -x "AZ_${SP_NAME_VAR}_OBJECT_ID=$(az ad sp list --display-name "$SP_NAME" --query "[].id" -o tsv)"

    echo "  ✅  Service Principal credentials exported!"
}
