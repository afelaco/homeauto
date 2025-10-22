data "azurerm_client_config" "this" {}

module "rg" {
  source = "./modules/resource_group"

  resource_group_name     = "${var.project_name}-rg"
  resource_group_location = var.location
}

module "kv" {
  source = "./modules/key_vault"

  key_vault_name      = "${var.project_name}-kv"
  key_vault_location  = module.rg.location
  tenant_id           = data.azurerm_client_config.this.tenant_id
  resource_group_name = module.rg.name

  sp_object_id = data.azurerm_client_config.this.object_id

  secrets = var.secrets
}

module "pypi" {
  source = "./modules/pypi"

  storage_account_name     = "${var.project_name}pypi"
  storage_account_location = module.rg.location
  resource_group_name      = module.rg.name
}

module "datalake" {
  source = "./modules/storage_account"

  for_each = toset(["bronze", "silver", "gold"])

  storage_account_name     = "${var.project_name}${each.key}sa"
  storage_account_location = module.rg.location
  resource_group_name      = module.rg.name

  container_name = ["steam"]

  role_assignment_id = module.kv.role_assignment_id
  key_vault_id       = module.kv.id
}

module "airflow_sp" {
  source = "./modules/service_principal"

  display_name = "airflow-sp"
  scope        = { (module.pypi.id) = "Storage Blob Data Contributor" }
}
