variable "storage_account_name" {
  description = "The name of the storage account."
  type        = string
}

variable "storage_account_location" {
  description = "The Azure region where the storage account will be created."
  type        = string
}

variable "resource_group_name" {
  description = "The name of the resource group in which to create the storage account."
  type        = string
}

variable "key_vault_id" {
  description = "The ID of the Key Vault where secrets will be stored."
  type        = string
}
