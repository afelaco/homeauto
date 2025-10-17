# terraform

This repository contains Terraform configurations to provision and manage Azure resources.

---

## Update Terraform State After Renaming a Module

When you rename a Terraform module, Terraform sees the new module block as a completely new resource by default. This
means it will try to create new resources and destroy the old ones unless you tell Terraform to map the old state to the
new module. Here’s how to handle it safely.

Suppose you originally had:

```tf
module "old_storage" {
  source              = "../modules/storage_account"
  name                = "myprojectsa"
  resource_group_name = module.rg.name
  location            = module.rg.location
}
```

And you rename it to:

```tf
module "storage_account" {
  source              = "./modules/storage_account"
  name                = "myprojectsa"
  resource_group_name = module.rg.name
  location            = module.rg.location
}
```

Terraform now sees `module.storage_account` as new and `module.old_storage` as orphaned. You need to move the state from
the old module to the new module. To get a list of the current state, run:

```bash
terraform state list
```

You should see something like:

```bash
module.old_storage.azurerm_storage_account.storage_account
```

Then, use the terraform state mv command to rename the module in the state file:

```bash
terraform state mv module.old_storage module.storage_account
```

This tells Terraform that the resources already exist under the new module name, preventing recreation. If you run
`terraform plan` after moving the state, it should show no changes (or only legitimate changes if you
modified the module).
