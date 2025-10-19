variable "project_name" {
  default = "homeauto"
  type    = string
}

variable "location" {
  default = "northeurope"
  type    = string
}

variable "kv_secrets" {
  type      = map(string)
  sensitive = true
}
