from dataclasses import dataclass
from typing import Literal

from src.airflow.core.dataset import Dataset


@dataclass
class SilverDataset(Dataset):
    storage_account: Literal["homeautosilversa"] = "homeautosilversa"

    def get_path(self) -> str:
        return f"abfss://{self.container}/{self.name}.parquet"
