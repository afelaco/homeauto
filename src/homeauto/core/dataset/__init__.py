from abc import ABC, abstractmethod
from dataclasses import dataclass

import polars as pl
from pandera.polars import DataFrameSchema

from homeauto.core.infra import StorageAccount
from homeauto.core.logger import get_logger

logger = get_logger(name=__name__)


@dataclass
class Dataset(ABC):
    name: str
    schema: DataFrameSchema
    container: str
    storage_account: StorageAccount

    @abstractmethod
    def get_path(self) -> str:
        pass

    def read_parquet(self) -> pl.DataFrame:
        source = self.get_path()
        df = pl.read_parquet(
            source=source,
            storage_options=self.storage_account.get_storage_options(),
        ).pipe(self.schema.validate)

        logger.info("%s records read from %s", len(df), source)

        return df

    def write_parquet(self, df: pl.DataFrame) -> None:
        file = self.get_path()
        df.pipe(self.schema.validate).write_parquet(
            file=file,
            storage_options=self.storage_account.get_storage_options(),
        )

        logger.info("%s records written to %s", len(df), file)
