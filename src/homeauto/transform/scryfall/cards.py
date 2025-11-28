import polars as pl

import homeauto.core.dataset.bronze.scryfall
import homeauto.core.dataset.silver.scryfall
from homeauto.core.dataset.bronze import BronzeDataset
from homeauto.core.dataset.silver import SilverDataset
from homeauto.transform import Transform


class TransformScryfallCards(Transform):
    @property
    def input_dataset(self) -> BronzeDataset:
        return homeauto.core.dataset.bronze.scryfall.cards

    @property
    def output_dataset(self) -> SilverDataset:
        return homeauto.core.dataset.silver.scryfall.cards

    @property
    def mapping(self) -> dict[str, str]:
        return {"id": "scryfall_id"}

    def run(self) -> None:
        self.output_dataset.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        return (
            self.input_dataset.read_parquet()
            .rename(mapping=self.mapping)
            .filter(~pl.col("digital"))
            .unnest("prices")
            .rename(
                {
                    "eur": "price",
                    "eur_foil": "price_foil",
                }
            )
            .select(self.output_dataset.schema.columns.keys())
        )


if __name__ == "__main__":
    TransformScryfallCards().run()
