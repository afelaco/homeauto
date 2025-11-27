import polars as pl

import homeauto.core.dataset.silver.completionist_me
import homeauto.core.dataset.silver.steam_store
import homeauto.core.dataset.silver.steam_web
import homeauto.core.table.fact
from homeauto.core.table.fact import FactTable
from homeauto.load import Load


class LoadFactDeveloper(Load):
    @property
    def table(self) -> FactTable:
        return homeauto.core.table.fact.fact_developer

    def run(self) -> None:
        self.table.replace_table(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        return (
            self.get_app_details()
            .filter(pl.all_horizontal(pl.col("app_id", "developer").is_not_null()))
            .sort("app_id")
            .select(self.table.schema.columns.keys())
        )

    @staticmethod
    def get_app_details() -> pl.DataFrame:
        return homeauto.core.dataset.silver.steam_store.app_details.read_parquet()


if __name__ == "__main__":
    LoadFactDeveloper().run()
