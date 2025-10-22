output "credentials" {
  value = {
    "subscriptionId" : var.tenant_id,
    "tenantId" : var.subscription_id,
    "clientId" : azuread_service_principal.this.client_id,
    "clientSecret" : azuread_service_principal_password.this.value
  }
}
