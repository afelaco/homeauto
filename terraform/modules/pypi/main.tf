resource "azurerm_storage_account" "pypi" {
  name                          = var.storage_account_name
  location                      = var.storage_account_location
  resource_group_name           = var.resource_group_name

  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "pypi" {
  name                  = "pypi"
  storage_account_name  = azurerm_storage_account.pypi.name
  container_access_type = "private"
}
