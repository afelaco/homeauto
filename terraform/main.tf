data "azurerm_client_config" "this" {}

module "rg" {
  source = "./modules/resource_group"

  resource_group_name     = "${var.project_name}-rg"
  resource_group_location = var.location
}

module "kv" {
  source = "./modules/key_vault"

  key_vault_name      = "${var.project_name}-kv"
  key_vault_location  = module.rg.resource_group_location
  tenant_id           = data.azurerm_client_config.this.tenant_id
  resource_group_name = module.rg.resource_group_name

  officers = {
    "User"             = var.admin_object_id
    "ServicePrincipal" = data.azurerm_client_config.this.object_id
  }

  secrets = var.secrets
}

module "datalake" {
  source = "./modules/storage_account"

  for_each = toset(["bronze", "silver", "gold"])

  storage_account_name     = "${var.project_name}${each.key}sa"
  storage_account_location = module.rg.resource_group_location
  resource_group_name      = module.rg.resource_group_name

  container_name = ["steam"]

  role_assignment_id = module.kv.role_assignment_id
  key_vault_id       = module.kv.key_vault_id
}

module "airflow_sp" {
  source = "./modules/service_principal"

  display_name = "airflow-sp"
  scope = {
    (module.datalake["bronze"].storage_account_id) = "Storage Blob Data Contributor"
    (module.datalake["silver"].storage_account_id) = "Storage Blob Data Contributor"
    (module.datalake["gold"].storage_account_id)   = "Storage Blob Data Contributor"
  }
}
