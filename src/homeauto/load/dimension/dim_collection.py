import polars as pl

import homeauto.core.dataset.silver.manabox
import homeauto.core.table.dimension
from homeauto.core.table.dimension import DimensionTable
from homeauto.load import Load


class LoadDimCollection(Load):
    @property
    def table(self) -> DimensionTable:
        return homeauto.core.table.dimension.dim_collection

    def run(self) -> None:
        self.table.replace_table(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        return self.get_collection().sort("name").select(self.table.schema.columns.keys())

    @staticmethod
    def get_collection() -> pl.DataFrame:
        return homeauto.core.dataset.silver.manabox.collection.read_parquet()


if __name__ == "__main__":
    LoadDimCollection().run()
