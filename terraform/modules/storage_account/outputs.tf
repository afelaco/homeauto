output "storage_account_name" { value = azurerm_storage_account.this.name }
output "storage_account_id" { value = azurerm_storage_account.this.id }
output "secret_name" { value = azurerm_key_vault_secret.this.name }
