import polars as pl
from tqdm import tqdm

import homeauto.core.dataset.bronze.steam_store
import homeauto.core.dataset.bronze.steam_web
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
        owned_games = self.get_owned_games().get_column("appid")
        data = []
        for app_id in tqdm(owned_games):
            params = {"appids": app_id}
            data.append(
                self.api_client.get(
                    endpoint=self.endpoint,
                    params=params,
                )
            )
        return pl.DataFrame(data=data)

    @staticmethod
    def get_owned_games() -> pl.DataFrame:
        return homeauto.core.dataset.bronze.steam_web.owned_games.read_parquet()


if __name__ == "__main__":
    data = ExtractSteamStoreAppDetails().get_data()
