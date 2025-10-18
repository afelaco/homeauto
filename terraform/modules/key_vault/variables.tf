variable "tenant_id" { type = string }
variable "resource_group_name" { type = string }
variable "key_vault_name" { type = string }
variable "key_vault_location" { type = string }
variable "admin_object_id" { type = string }
variable "sp_object_id" { type = string }

# Secrets
variable "steam_id" {
  type      = string
  sensitive = true
}
variable "steam_key" {
  type      = string
  sensitive = true
}
