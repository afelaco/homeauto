from dataclasses import dataclass

from homeauto.core.dataset import Dataset
from homeauto.core.infra import infra


@dataclass
class SilverDataset(Dataset):
    storage_account: str = infra.datalake.silver

    def get_path(self) -> str:
        return f"abfss://{self.container}/{self.name}.parquet"
