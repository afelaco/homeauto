# Project
variable "project_name" {
  description = "Prefix for resource names"
  type        = string
  default     = "homeauto"
}

# Azure
variable "location" {
  description = "Azure region"
  type        = string
  default     = "northeurope"
}

variable "tenant_id" {
  description = "Azure Tenant ID"
  type        = string
  default     = "1d5073f8-a416-4dd0-8cf4-6926871926db"
  sensitive   = true
}

variable "subscription_id" {
  description = "Azure Subscription ID"
  type        = string
  default     = "883b4338-8b8b-4634-b2c7-c200e29303b7"
  sensitive   = true
}

# Architecture
variable "layers" {
  description = "List of storage account layers"
  type        = list(string)
  default     = ["bronze", "silver", "gold"]
}
