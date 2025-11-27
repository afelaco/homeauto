import polars as pl

import homeauto.core.dataset.silver.completionist_me
import homeauto.core.dataset.silver.steam_store
import homeauto.core.dataset.silver.steam_web
import homeauto.core.table.dimension
from homeauto.core.table.dimension import DimensionTable
from homeauto.load import Load


class LoadDimOwnedGames(Load):
    @property
    def table(self) -> DimensionTable:
        return homeauto.core.table.dimension.dim_owned_games

    def run(self) -> None:
        self.table.replace_table(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        return (
            self.get_owned_games()
            .join(
                other=self.get_steam_app(),
                on="app_id",
                how="left",
            )
            .join(
                other=self.get_app_details(),
                on="app_id",
                how="left",
            )
            .unique("app_id")
            .sort("app_id")
            .select(self.table.schema.columns.keys())
        )

    @staticmethod
    def get_app_details() -> pl.DataFrame:
        return homeauto.core.dataset.silver.steam_store.app_details.read_parquet()

    @staticmethod
    def get_owned_games() -> pl.DataFrame:
        return homeauto.core.dataset.silver.steam_web.owned_games.read_parquet()

    @staticmethod
    def get_steam_app() -> pl.DataFrame:
        return homeauto.core.dataset.silver.completionist_me.steam_app.read_parquet()


if __name__ == "__main__":
    LoadDimOwnedGames().run()
