import polars as pl

import homeauto.core.dataset.bronze.hltb
import homeauto.core.dataset.bronze.steam
import homeauto.core.endpoint.hltb
from homeauto.core.dataset.bronze import BronzeDataset
from homeauto.core.endpoint import Endpoint
from homeauto.extract.hltb import ExtractHltb


class ExtractHltbSearch(ExtractHltb):
    @property
    def endpoint(self) -> Endpoint:
        return homeauto.core.endpoint.hltb.search

    @property
    def dataset(self) -> BronzeDataset:
        return homeauto.core.dataset.bronze.hltb.search

    def run(self) -> None:
        self.dataset.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        owned_games = homeauto.core.dataset.bronze.steam.owned_games.read_parquet().get_column("name")
        params = {"names": owned_games.to_list()[:3]}
        self.api_client.get(
            endpoint=self.endpoint,
            params=params,
        )
        return pl.DataFrame(data=data)


if __name__ == "__main__":
    data = ExtractHltbSearch().get_data()
