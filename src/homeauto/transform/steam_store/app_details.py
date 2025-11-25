import polars as pl

import homeauto.core.dataset.bronze.steam_store
import homeauto.core.dataset.silver.steam_store
from homeauto.core.dataset.bronze import BronzeDataset
from homeauto.core.dataset.silver import SilverDataset
from homeauto.transform import Transform


class TransformSteamStoreAppDetails(Transform):
    @property
    def input_dataset(self) -> BronzeDataset:
        return homeauto.core.dataset.bronze.steam_store.app_details

    @property
    def output_dataset(self) -> SilverDataset:
        return homeauto.core.dataset.silver.steam_store.app_details

    @property
    def mapping(self) -> dict[str, str]:
        return {
            "steam_appid": "app_id",
            "metacritic": "score",
        }

    def run(self) -> None:
        self.output_dataset.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        return (
            self.input_dataset.read_parquet()
            .rename(self.mapping)
            .filter(pl.all_horizontal(pl.all().is_not_null()))
            .sort("score")
            .unique("app_id")
            .select(self.output_dataset.schema.columns.keys())
        )


if __name__ == "__main__":
    TransformSteamStoreAppDetails().run()
