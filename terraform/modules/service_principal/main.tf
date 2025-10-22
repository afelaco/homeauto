resource "azuread_application" "this" {
  display_name = var.display_name
}

resource "azuread_service_principal" "this" {
  client_id = azuread_application.this.client_id
}

resource "time_rotating" "month" {
  rotation_days = 30
}

resource "azuread_service_principal_password" "this" {
  service_principal_id = azuread_service_principal.this.object_id
  rotate_when_changed  = { rotation = time_rotating.month.id }
}

resource "azurerm_role_assignment" "this" {
  for_each = var.scope

  scope                = each.key
  role_definition_name = each.value
  principal_id         = azuread_service_principal.this.object_id
}
