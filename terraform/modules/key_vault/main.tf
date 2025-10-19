resource "azurerm_key_vault" "this" {
  name                = var.key_vault_name
  location            = var.key_vault_location
  tenant_id           = var.tenant_id
  resource_group_name = var.resource_group_name

  sku_name                  = "standard"
  enable_rbac_authorization = true
}

resource "azurerm_role_assignment" "this" {
  principal_id         = var.sp_object_id
  principal_type       = "ServicePrincipal"
  role_definition_name = "Key Vault Secrets Officer"
  scope                = azurerm_key_vault.this.id
}

resource "azurerm_key_vault_secret" "steam_id" {
  depends_on = [azurerm_role_assignment.this]

  for_each = toset(var.external_secrets)

  name         = each.key
  value        = each.value
  key_vault_id = azurerm_key_vault.this.id
}
