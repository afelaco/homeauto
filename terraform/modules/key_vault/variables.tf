variable "key_vault_name" {
  description = "The name of the key vault."
  type        = string
}

variable "key_vault_location" {
  description = "The Azure region where the key vault will be created."
  type        = string
}

variable "resource_group_name" {
  description = "The name of the resource group in which to create the key vault."
  type        = string
}

variable "tenant_id" {
  description = "The Tenant ID for the Key Vault."
  type        = string
}

variable "admin_object_id" {
  description = "The Object ID of the admin to assign roles."
  type        = string
  default     = "0a909171-669b-492b-bd9b-c1f777a42f23"
  sensitive   = true
}

variable "sp_object_id" {
  description = "The Object ID of the admin to assign roles."
  type        = string
  default     = "47ebeced-3e04-4eaf-98e5-075236b4009f"
  sensitive   = true
}

variable "secrets" {
  description = "Secrets to sync to Key Vault"
  type        = map(string)
}
