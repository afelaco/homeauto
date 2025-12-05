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
        data = (
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
            .with_columns(pl.col("collector_number").cast(pl.Int64, strict=False))
            .filter(pl.col("collector_number").is_not_null())
        )

        max_collector_number = (
            data.filter(pl.col("name").eq("Forest"))
            .sort("collector_number")
            .unique(
                "set",
                keep="last",
            )
            .select("set", "collector_number")
            .rename({"collector_number": "max_collector_number"})
        )

        return (
            data.join(
                other=max_collector_number,
                on="set",
                how="left",
            )
            .filter(pl.col("collector_number") <= pl.col("max_collector_number"))
            .select(self.output_dataset.schema.columns.keys())
        )


if __name__ == "__main__":
    TransformScryfallCards().run()
