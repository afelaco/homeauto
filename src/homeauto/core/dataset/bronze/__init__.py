from dataclasses import dataclass, field

from homeauto.core.dataset import Dataset
from homeauto.core.infra import StorageAccount, infra


@dataclass
class BronzeDataset(Dataset):
    storage_account: StorageAccount = field(default_factory=lambda: infra.datalake.bronze)

    def get_path(self) -> str:
        return f"abfss://{self.container}/{self.name}.parquet"
