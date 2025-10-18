# Config
variable "project_name" {
  type    = string
  default = "homeauto"
}

variable "location" {
  type    = string
  default = "northeurope"
}

# .env
variable "tenant_id" { type = string }
variable "subscription_id" { type = string }
variable "admin_object_id" { type = string }
variable "sp_object_id" { type = string }
variable "steam_id" {
  type      = string
  sensitive = true
}
variable "steam_key" {
  type      = string
  sensitive = true
}
