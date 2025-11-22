import polars as pl

import homeauto.core.dataset.bronze.steam
import homeauto.core.endpoint.steam_store
from homeauto.core.dataset.bronze import BronzeDataset
from homeauto.core.endpoint import Endpoint
from homeauto.extract.steam_store import ExtractSteamStore


class ExtractSteamStoreAppDetails(ExtractSteamStore):
    @property
    def endpoint(self) -> Endpoint:
        return homeauto.core.endpoint.steam_store.appdetails

    @property
    def dataset(self) -> BronzeDataset:
        return homeauto.core.dataset.bronze.steam_store.app_details

    def run(self) -> None:
        self.dataset.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        params = {"appids": "10"}
        data = self.api_client.get(
            endpoint=self.endpoint,
            params=params,
        )
        return pl.DataFrame(data=data)


if __name__ == "__main__":
    data = ExtractSteamStoreAppDetails().get_data().to_pandas()
