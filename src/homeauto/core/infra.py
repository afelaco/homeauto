import json

from pydantic import BaseModel


class DataLake(BaseModel):
    bronze: str
    silver: str
    gold: str


class Infrastructure(BaseModel):
    datalake: DataLake


path = "infra.json"
with open(path) as f:
    infra_json = {k: v["value"] for k, v in json.load(f).items()}

infra = Infrastructure.model_validate(infra_json)
