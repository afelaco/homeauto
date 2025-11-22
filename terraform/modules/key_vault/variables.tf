variable "tenant_id" { type = string }
variable "resource_group_name" { type = string }
variable "key_vault_name" { type = string }
variable "key_vault_location" { type = string }
variable "officers" {
  type      = map(string)
  sensitive = true
}
variable "secrets" {
  type      = map(string)
  sensitive = true
}
