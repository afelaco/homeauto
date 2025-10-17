import polars as pl

import homeauto.core.dataset.bronze.steam
import homeauto.core.dataset.gold.steam
import homeauto.core.endpoint.steam
from homeauto.core.dataset.bronze import BronzeDataset
from homeauto.core.endpoint import Endpoint
from homeauto.core.logger import get_logger
from homeauto.extract.steam import ExtractSteam

logger = get_logger(name=__name__)


class ExtractSteamPlayerAchievements(ExtractSteam):
    @property
    def endpoint(self) -> Endpoint:
        return homeauto.core.endpoint.steam.player_achievements

    @property
    def dataset(self) -> BronzeDataset:
        return homeauto.core.dataset.bronze.steam.player_achievements

    def run(self) -> None:
        self.dataset.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        data = []
        played_games = self.get_played_games()
        for id in played_games["id"]:
            try:
                data.extend(
                    self.api_client.get(
                        endpoint=self.endpoint,
                        params={"appid": id},
                    )
                )
            except Exception:
                continue
        return pl.DataFrame(data=data)

    @staticmethod
    def get_played_games() -> pl.DataFrame:
        return homeauto.core.dataset.gold.steam.dim_owned_games.read_parquet().filter(pl.col("playtime") > 0)


if __name__ == "__main__":
    ExtractSteamPlayerAchievements().run()
