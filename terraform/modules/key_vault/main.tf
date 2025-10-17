resource "azurerm_key_vault" "this" {
  name                = var.key_vault_name
  location            = var.key_vault_location
  resource_group_name = var.resource_group_name
  tenant_id           = var.tenant_id

  sku_name                  = "standard"
  enable_rbac_authorization = true
}

# Set roles for the Key Vault.
resource "azurerm_role_assignment" "admin" {
  depends_on = [azurerm_key_vault.this]

  scope                = azurerm_key_vault.this.id
  role_definition_name = "Key Vault Secrets Officer"
  principal_id         = var.admin_object_id
}

resource "azurerm_role_assignment" "sp" {
  depends_on = [azurerm_key_vault.this]

  scope                = azurerm_key_vault.this.id
  role_definition_name = "Key Vault Secrets Officer"
  principal_id         = var.sp_object_id
  principal_type       = "ServicePrincipal"
}

# Set external secrets.
resource "azurerm_key_vault_secret" "this" {
  depends_on = [azurerm_role_assignment.sp]

  for_each = var.secrets

  name         = each.key
  value        = each.value
  key_vault_id = azurerm_key_vault.this.id
}
