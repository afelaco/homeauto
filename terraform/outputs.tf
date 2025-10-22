output "pypi_storage_account" { value = module.pypi.name }
output "pypi_container" { value = module.pypi.container_name }

output "keyvault" {
  value = {
    uri = module.kv.uri
  }
}

output "datalake" {
  value = {
    for k, m in module.datalake : k => {
      name   = m.storage_account_name
      secret = m.secret_name
    }
  }
}

output "airflow_sp_creds" {
  value     = module.airflow-sp.credentials
  sensitive = true
}
