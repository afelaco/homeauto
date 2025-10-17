from dataclasses import dataclass
from typing import Literal

from homeauto.core.dataset import Dataset


@dataclass
class GoldDataset(Dataset):
    storage_account: Literal["homeautogoldsa"] = "homeautogoldsa"

    def get_path(self) -> str:
        return f"abfss://{self.container}/{self.name}.parquet"
