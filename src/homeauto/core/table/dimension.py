from abc import ABC

from pandera.polars import Column, DataFrameSchema
from polars import Boolean, Int64, String

from homeauto.core.infra import Database
from homeauto.core.table import Table


class DimensionTable(Table, ABC):
    pass


dim_app_details = DimensionTable(
    name="dim_app_details",
    schema=DataFrameSchema(
        columns={
            "app_id": Column(String),
            "name": Column(String),
            "short_description": Column(String),
            "about_the_game": Column(String),
            "detailed_description": Column(String),
            "metacritic": Column(Int64, nullable=True),
            "is_free": Column(Boolean),
            "initial_price": Column(Int64, nullable=True),
            "final_price": Column(Int64, nullable=True),
            "currency": Column(String, nullable=True),
            "discount_percent": Column(Int64, nullable=True),
            "release_date": Column(String),
            "coming_soon": Column(Boolean),
        },
        strict=True,
    ),
    database=Database(),
)
dim_owned_games = DimensionTable(
    name="dim_owned_games",
    schema=DataFrameSchema(
        columns={
            "app_id": Column(String, unique=True),
            "name": Column(String),
            "playtime": Column(Int64),
            "score": Column(Int64, nullable=True),
            "completion_time": Column(Int64, nullable=True),
        },
        strict=True,
    ),
    database=Database(),
)
