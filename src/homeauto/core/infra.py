import json

from pydantic import BaseModel

from homeauto.core.utils import get_secret


class StorageAccount(BaseModel):
    name: str
    secret: str

    def get_storage_options(self) -> dict[str, str]:
        return {
            "account_name": self.name,
            "account_key": get_secret(self.secret),
        }


class DataLake(BaseModel):
    bronze: StorageAccount
    silver: StorageAccount
    gold: StorageAccount


class Infrastructure(BaseModel):
    datalake: DataLake


path = "infra.json"
with open(path) as f:
    infra_json = {k: v["value"] for k, v in json.load(f).items()}

infra = Infrastructure.model_validate(infra_json)
