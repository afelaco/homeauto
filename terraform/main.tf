# Terraform Backend
terraform {
  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "homeautobackend"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}

# Resource Groups
module "rg" {
  source                  = "./modules/resource_group"
  resource_group_name     = "${var.project_name}-rg"
  resource_group_location = var.location
}

# Key Vault
module "kv" {
  source              = "./modules/key_vault"
  tenant_id           = var.tenant_id
  resource_group_name = module.rg.name
  key_vault_name      = "${var.project_name}-kv"
  key_vault_location  = module.rg.location
  admin_object_id     = var.admin_object_id
  sp_object_id        = var.sp_object_id
  steam_id            = var.steam_id
  steam_key           = var.steam_key
}

# PyPI
module "pypi" {
  source                   = "./modules/pypi"
  storage_account_name     = "${var.project_name}pypi"
  storage_account_location = module.rg.location
  resource_group_name      = module.rg.name
}

# Storage Accounts
module "datalake" {
  for_each = toset(["bronze", "silver", "gold"])

  source                   = "./modules/storage_account"
  storage_account_name     = "${var.project_name}${each.key}sa"
  storage_account_location = module.rg.location
  resource_group_name      = module.rg.name
  key_vault_id             = module.kv.id
}
