from abc import ABC

from pandera.polars import Column, DataFrameSchema
from polars import String

from homeauto.core.infra import Database
from homeauto.core.table import Table


class FactTable(Table, ABC):
    pass


fact_categories = FactTable(
    name="fact_categories",
    schema=DataFrameSchema(
        columns={
            "app_id": Column(String),
            "category_id": Column(String),
        },
        strict=True,
    ),
    database=Database(),
)

fact_genres = FactTable(
    name="fact_genres",
    schema=DataFrameSchema(
        columns={
            "app_id": Column(String),
            "genre_id": Column(String),
        },
        strict=True,
    ),
    database=Database(),
)

fact_owned_games_tags = FactTable(
    name="fact_owned_games_tags",
    schema=DataFrameSchema(
        columns={
            "id": Column(str),
            "tag": Column(str, nullable=True),
        },
        strict=True,
    ),
    database=Database(),
)
