import polars as pl

import homeauto.core.dataset.bronze.steam
import homeauto.core.endpoint.steam
from homeauto.core.dataset.bronze import BronzeDataset
from homeauto.core.endpoint import Endpoint
from homeauto.extract.steam import ExtractSteam


class ExtractSteamOwnedGames(ExtractSteam):
    @property
    def endpoint(self) -> Endpoint:
        return homeauto.core.endpoint.steam.owned_games

    @property
    def dataset(self) -> BronzeDataset:
        return homeauto.core.dataset.bronze.steam.owned_games

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
    data = ExtractSteamOwnedGames().get_data().to_pandas()
