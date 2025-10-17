import polars as pl

import src.airflow.core.dataset.gold.steam
import src.airflow.core.dataset.silver.steam
from src.airflow.core.dataset.gold import GoldDataset
from src.airflow.scripts.load import Load


class LoadDimOwnedGames(Load):
    @property
    def output_dataset(self) -> GoldDataset:
        return src.airflow.core.dataset.gold.steam.dim_owned_games

    def run(self) -> None:
        self.output_dataset.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        return (
            src.airflow.core.dataset.silver.steam.owned_games.read_parquet()
            .unique("id")
            .select(self.output_dataset.schema.columns.keys())
        )


if __name__ == "__main__":
    LoadDimOwnedGames().run()
