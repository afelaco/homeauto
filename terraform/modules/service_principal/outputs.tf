output "client_id" { value = azuread_service_principal.this.client_id }
output "client_secret" {
  value     = azuread_service_principal_password.this.value
  sensitive = true
}
