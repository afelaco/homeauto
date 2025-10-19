data "azurerm_client_config" "this" {}

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=4.1.0"
    }
  }
}

provider "azurerm" {
  subscription_id = data.azurerm_client_config.this.subscription_id
  features {}
}
