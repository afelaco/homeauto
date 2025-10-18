output "pypi" {
  value = {
    storage_account = module.pypi.name
    container       = module.pypi.container_name
  }
}

output "datalake" {
  value = {
    for k, m in module.datalake : k => {
      storage_account = m.storage_account_name
      secret          = m.secret_name
    }
  }
}
