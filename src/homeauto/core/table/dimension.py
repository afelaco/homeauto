from abc import ABC

from pandera.polars import Column, DataFrameSchema
from polars import Boolean, Date, Int64, String

from homeauto.core.infra import Database
from homeauto.core.table import Table


class DimensionTable(Table, ABC):
    pass


dim_app_details = DimensionTable(
    name="dim_app_details",
    schema=DataFrameSchema(
        columns={
            "app_id": Column(String),
            "short_description": Column(String),
            "about_the_game": Column(String),
            "detailed_description": Column(String),
            "metacritic": Column(Int64, nullable=True),
            "is_free": Column(Boolean),
            "initial_price": Column(Int64, nullable=True),
            "final_price": Column(Int64, nullable=True),
            "currency": Column(String, nullable=True),
            "discount_percent": Column(Int64, nullable=True),
            "release_date": Column(Date, nullable=True),
            "coming_soon": Column(Boolean),
        },
        strict=True,
    ),
    database=Database(),
)

dim_completion = DimensionTable(
    name="dim_completion",
    schema=DataFrameSchema(
        columns={
            "app_id": Column(str, unique=True),
            "completion_time": Column(int),
        },
        strict=True,
    ),
    database=Database(),
)

dim_genre = DimensionTable(
    name="dim_genre",
    schema=DataFrameSchema(
        columns={
            "genre_id": Column(String, unique=True),
            "genre_description": Column(String),
        },
        strict=True,
    ),
    database=Database(),
)

dim_category = DimensionTable(
    name="dim_category",
    schema=DataFrameSchema(
        columns={
            "category_id": Column(String, unique=True),
            "category_description": Column(String),
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
        },
        strict=True,
    ),
    database=Database(),
)
