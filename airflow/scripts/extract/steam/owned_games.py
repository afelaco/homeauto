import polars as pl

import src.airflow.core.dataset.bronze.steam
import src.airflow.core.endpoint.steam
from src.airflow.core.dataset.bronze import BronzeDataset
from src.airflow.core.endpoint import Endpoint
from src.airflow.scripts.extract.steam import ExtractSteam


class ExtractSteamOwnedGames(ExtractSteam):
    @property
    def endpoint(self) -> Endpoint:
        return src.airflow.core.endpoint.steam.owned_games

    @property
    def dataset(self) -> BronzeDataset:
        return src.airflow.core.dataset.bronze.steam.owned_games

    def run(self) -> None:
        self.dataset.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        params = {"include_appinfo": "true"}
        data = self.api_client.get(
            endpoint=self.endpoint,
            params=params,
        )
        return pl.DataFrame(data=data)


if __name__ == "__main__":
    ExtractSteamOwnedGames().run()
