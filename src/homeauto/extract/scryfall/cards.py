import polars as pl

import homeauto.core.dataset.bronze.scryfall
import homeauto.core.dataset.silver.steam_web
import homeauto.core.endpoint.scryfall
from homeauto.core import get_logger
from homeauto.core.dataset.bronze import BronzeDataset
from homeauto.core.endpoint import Endpoint
from homeauto.extract.scryfall import ExtractScryfall

logger = get_logger(name=__name__)

SETS = [
    "KHM",
    "THB",
    "MOM",
    "TDM",
    "ONE",
    "DFT",
    "WOE",
    "VOW",
    "ELD",
    "MID",
    "AFR",
    "DOM",
    "MKM",
    "DSK",
    "ZNR",
    "LCI",
    "SNC",
    "EOE",
    "OTJ",
    "WAR",
    "NEO",
    "STX",
    "BLB",
    "BRO",
    "DMU",
    "IKO",
    "GRN",
    "RNA",
]


class ExtractScryfallCards(ExtractScryfall):
    @property
    def endpoint(self) -> Endpoint:
        return homeauto.core.endpoint.scryfall.cards

    @property
    def dataset(self) -> BronzeDataset:
        return homeauto.core.dataset.bronze.scryfall.cards

    def run(self) -> None:
        self.dataset.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        data = []
        for set in SETS:
            params = {"q": f"set:{set}"}
            data.extend(
                self.api_client.get(
                    endpoint=self.endpoint,
                    params=params,
                )
            )
        return pl.DataFrame(
            data=data,
            infer_schema_length=len(data),
        )


if __name__ == "__main__":
    ExtractScryfallCards().run()
