import polars as pl

import homeauto.core.dataset.gold.steam_web
import homeauto.core.dataset.silver.steam_web
from homeauto.core.dataset.gold import GoldDataset
from homeauto.load import Load


class LoadFactOwnedGamesTags(Load):
    @property
    def output_dataset(self) -> GoldDataset:
        return homeauto.core.dataset.gold.steam_web.fact_owned_games_tags

    def run(self) -> None:
        self.output_dataset.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        return (
            homeauto.core.dataset.silver.steam_web.owned_games.read_parquet()
            .filter(pl.col("tag").is_not_null())
            .select(self.output_dataset.schema.columns.keys())
        )


if __name__ == "__main__":
    LoadFactOwnedGamesTags().run()
