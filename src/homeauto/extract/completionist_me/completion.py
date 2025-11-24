import polars as pl
from tqdm import tqdm

import homeauto.core.dataset.bronze.completionist_me
import homeauto.core.dataset.bronze.steam
from homeauto.core.dataset.bronze import BronzeDataset
from homeauto.extract.completionist_me import ExtractCompletionistMe


class ExtractCompletionPlaytimeAvg(ExtractCompletionistMe):
    @property
    def dataset(self) -> BronzeDataset:
        return homeauto.core.dataset.bronze.completionist_me.completion_playtime_avg

    def run(self) -> None:
        self.dataset.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        owned_games = homeauto.core.dataset.bronze.steam.owned_games.read_parquet().get_column("appid")
        data = []
        for app_id in tqdm(owned_games):
            data.append(self.scraper.find_next(app_id=app_id))
        return pl.DataFrame(data=data)


if __name__ == "__main__":
    data = ExtractCompletionPlaytimeAvg().get_data()
