output "pypi" {
  value = {
    storage_account = module.pypi.name
    container       = module.pypi.container_name
  }
}

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
