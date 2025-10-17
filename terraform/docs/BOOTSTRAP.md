# Bootstrap

This document describes the steps required to bootstrap the environment for the project.

---

# Bootstrap `.config.sh` File

The `.config.sh` file contains the configuration variables required for the bootstrap process. It is ignored by Git as
it
may contain sensitive information, so you need to create it manually.

---

# Terraform `tfvars` File

The `terraform.tfvars` file contains sensitive variables required at runtime by Terraform. It is ignored by Git as it
may contain sensitive information, so you need to create it manually.
---

# GitHub

It is required to manually create
a [GitHub Personal Access Token (PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
with the following scopes:

- `repo`
- `workflow`
- `read:org`

The token is then stored in `config.sh` as `GITHUB_TOKEN`.

---

# Azure

> When a new Service Principal is created, both a Service Principal Object and an Application Object are created with
> different IDs. The Service Principal Object ID required to set permissions in the Key Vault is found under Enterprise
> Applications in the Azure Portal!

Once the Service Principal is created via the bootstrap script, find its Object ID under
`bootstrap/artifacts/az-sp-object-id.txt`. Copy its value to a `sp_object_id` sensitive variable in the
`.modules/key_vault/variables.tf` file:

```hcl
variable "object_id" {
  description = "Object ID of the service principal"
  type        = string
  default     = "00000000-0000-0000-0000-000000000000"
  sensitive   = true
}
```

---

# Docs

> [Homebrew Bundle](https://docs.brew.sh/Brew-Bundle-and-Brewfile).

> [Git](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git).
