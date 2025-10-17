from functools import lru_cache
from typing import Any

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

from homeauto.core.logger import get_logger

logger = get_logger(name=__name__)


@lru_cache
def get_secret(secret_name: str) -> Any:
    key_vault_name = "homeauto-kv"
    key_vault_url = f"https://{key_vault_name}.vault.azure.net"

    value = (
        SecretClient(
            vault_url=key_vault_url,
            credential=DefaultAzureCredential(),
        )
        .get_secret(name=secret_name)
        .value
    )

    logger.info("%s read from %s", secret_name, key_vault_url)

    return value
