from pandera.polars import Column, DataFrameSchema
from polars import Boolean, Float64, Int64, String

from homeauto.core.dataset.silver import SilverDataset

collection = SilverDataset(
    container="manabox",
    name="collection",
    schema=DataFrameSchema(
        columns={
            "name": Column(String),
            "set_code": Column(String),
            "set_name": Column(String),
            "collector_number": Column(Int64),
            "foil": Column(String),
            "rarity": Column(String),
            "quantity": Column(Int64),
            "manabox_id": Column(Int64),
            "scryfall_id": Column(String),
            "purchase_price": Column(Float64),
            "misprint": Column(Boolean),
            "altered": Column(Boolean),
            "condition": Column(String),
            "language": Column(String),
            "purchase_price_currency": Column(String),
        },
        strict=True,
    ),
)
