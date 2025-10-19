variable "project_name" {
  default = "homeauto"
  type    = string
}

variable "location" {
  default = "northeurope"
  type    = string
}

variable "external_secrets" {
  type      = map(string)
  sensitive = true
}

locals {
  external_secrets = jsondecode(var.external_secrets)
}
