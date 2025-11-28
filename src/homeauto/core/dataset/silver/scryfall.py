from pandera.polars import Column, DataFrameSchema
from polars import Boolean, Float64, String

from homeauto.core.dataset.silver import SilverDataset

cards = SilverDataset(
    container="scryfall",
    name="cards",
    schema=DataFrameSchema(
        columns={
            "scryfall_id": Column(String, unique=True),
            "name": Column(String),
            "set": Column(String),
            "set_name": Column(String),
            "collector_number": Column(String),
            "released_at": Column(String),
            "layout": Column(String),
            "cmc": Column(Float64),
            "type_line": Column(String),
            "oracle_text": Column(String, nullable=True),
            "power": Column(String, nullable=True),
            "toughness": Column(String, nullable=True),
            "reserved": Column(Boolean),
            "game_changer": Column(Boolean),
            "foil": Column(Boolean),
            "nonfoil": Column(Boolean),
            "oversized": Column(Boolean),
            "promo": Column(Boolean),
            "reprint": Column(Boolean),
            "variation": Column(Boolean),
            "rarity": Column(String),
            "full_art": Column(Boolean),
            "textless": Column(Boolean),
            "booster": Column(Boolean),
            "price": Column(String, nullable=True),
            "price_foil": Column(String, nullable=True),
        },
        strict=True,
    ),
)
