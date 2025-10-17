import polars as pl

import src.airflow.core.dataset.bronze.steam
import src.airflow.core.dataset.silver.steam
from src.airflow.core.dataset.bronze import BronzeDataset
from src.airflow.core.dataset.silver import SilverDataset
from src.airflow.scripts.transform import Transform


class TransformSteamOwnedGames(Transform):
    @property
    def input_dataset(self) -> BronzeDataset:
        return src.airflow.core.dataset.bronze.steam.owned_games

    @property
    def output_dataset(self) -> SilverDataset:
        return src.airflow.core.dataset.silver.steam.owned_games

    @property
    def mapping(self) -> dict[str, str]:
        return {
            "appid": "id",
            "playtime_forever": "playtime",
            "content_descriptorids": "tag",
        }

    def run(self) -> None:
        self.output_dataset.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        return (
            self.input_dataset.read_parquet()
            .rename(self.mapping)
            .explode("tag")
            .with_columns(pl.col("id", "tag").cast(pl.String))
            .select(self.output_dataset.schema.columns.keys())
        )


if __name__ == "__main__":
    TransformSteamOwnedGames().run()
