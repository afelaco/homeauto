import polars as pl

import homeauto.core.dataset.silver.steam_web
import homeauto.core.table.fact
from homeauto.core.table.fact import FactTable
from homeauto.load import Load


class LoadFactOwnedGamesTags(Load):
    @property
    def table(self) -> FactTable:
        return homeauto.core.table.fact.fact_owned_games_tags

    def run(self) -> None:
        self.table.replace_table(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        return (
            homeauto.core.dataset.silver.steam_web.owned_games.read_parquet()
            .filter(pl.col("tag").is_not_null())
            .select(self.table.schema.columns.keys())
        )


if __name__ == "__main__":
    LoadFactOwnedGamesTags().run()
