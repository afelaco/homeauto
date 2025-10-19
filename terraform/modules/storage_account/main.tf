resource "azurerm_storage_account" "this" {
  name                = var.storage_account_name
  location            = var.storage_account_location
  resource_group_name = var.resource_group_name

  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "this" {
  for_each = toset(var.container_name)

  name                 = each.key
  storage_account_name = azurerm_storage_account.this.name
}

resource "azurerm_key_vault_secret" "this" {
  name         = "${upper(azurerm_storage_account.this.name)}-KEY"
  value        = azurerm_storage_account.this.primary_access_key
  key_vault_id = var.key_vault_id
}
