output "pypi" {
  value = jsonencode({
    name      = module.pypi.name
    container = module.pypi.container_name
  })
}

output "infrastructure" {
  value = jsonencode(
    {
      keyvault = {
        uri = module.kv.uri
      }
      datalake = {
        bronze = {
          name   = module.datalake["bronze"].storage_account_name
          secret = module.datalake["bronze"].secret_name
        }
        silver = {
          name   = module.datalake["silver"].storage_account_name
          secret = module.datalake["silver"].secret_name
        }
        gold = {
          name   = module.datalake["gold"].storage_account_name
          secret = module.datalake["gold"].secret_name
        }
      }
    }
  )
}

output "airflow_sp_creds" {
  value = jsonencode({
    tenantId       = data.azurerm_client_config.this.tenant_id
    subscriptionId = data.azurerm_client_config.this.subscription_id
    clientId       = module.airflow_sp.client_id
    clientSecret   = module.airflow_sp.client_secret
  })
  sensitive = true
}
