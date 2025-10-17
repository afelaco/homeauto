import polars as pl

import src.airflow.core.dataset.bronze.steam
import src.airflow.core.dataset.gold.steam
import src.airflow.core.endpoint.steam
from src.airflow.core.dataset.bronze import BronzeDataset
from src.airflow.core.endpoint import Endpoint
from src.airflow.core.logger import get_logger
from src.airflow.scripts.extract.steam import ExtractSteam

logger = get_logger(name=__name__)


class ExtractSteamPlayerAchievements(ExtractSteam):
    @property
    def endpoint(self) -> Endpoint:
        return src.airflow.core.endpoint.steam.player_achievements

    @property
    def dataset(self) -> BronzeDataset:
        return src.airflow.core.dataset.bronze.steam.player_achievements

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
        return src.airflow.core.dataset.gold.steam.dim_owned_games.read_parquet().filter(pl.col("playtime") > 0)


if __name__ == "__main__":
    ExtractSteamPlayerAchievements().run()
