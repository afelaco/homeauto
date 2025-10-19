variable "project_name" {
  default = "homeauto"
  type    = string
}

variable "subscription_id" {
  type      = string
  sensitive = true
}

variable "location" {
  default = "northeurope"
  type    = string
}

variable "secrets" {
  type      = map(string)
  sensitive = true
}
