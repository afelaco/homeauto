import polars as pl

import homeauto.core.dataset.gold.steam_web
import homeauto.core.dataset.silver.steam_web
from homeauto.core.dataset.gold import GoldDataset
from homeauto.load import Load


class LoadDimOwnedGames(Load):
    @property
    def output_dataset(self) -> GoldDataset:
        return homeauto.core.dataset.gold.steam_web.dim_owned_games

    def run(self) -> None:
        self.output_dataset.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        return (
            homeauto.core.dataset.silver.steam_web.owned_games.read_parquet()
            .unique("id")
            .select(self.output_dataset.schema.columns.keys())
        )


if __name__ == "__main__":
    LoadDimOwnedGames().run()
