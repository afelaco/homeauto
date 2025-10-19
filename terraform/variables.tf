variable "project_name" {
  default = "homeauto"
  type    = string
}

variable "location" {
  default = "northeurope"
  type    = string
}

variable "secrets" { type = map(string) }
