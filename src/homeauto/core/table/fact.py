from abc import ABC

from pandera.polars import Column, DataFrameSchema
from polars import String

from homeauto.core.infra import Database
from homeauto.core.table import Table


class FactTable(Table, ABC):
    pass


fact_category = FactTable(
    name="fact_category",
    schema=DataFrameSchema(
        columns={
            "app_id": Column(String),
            "category_id": Column(String),
        },
        strict=True,
    ),
    database=Database(),
)

fact_developer = FactTable(
    name="fact_developer",
    schema=DataFrameSchema(
        columns={
            "app_id": Column(String),
            "developer": Column(String),
        },
        strict=True,
    ),
    database=Database(),
)

fact_genre = FactTable(
    name="fact_genre",
    schema=DataFrameSchema(
        columns={
            "app_id": Column(String),
            "genre_id": Column(String),
        },
        strict=True,
    ),
    database=Database(),
)

fact_publisher = FactTable(
    name="fact_publisher",
    schema=DataFrameSchema(
        columns={
            "app_id": Column(String),
            "publisher": Column(String),
        },
        strict=True,
    ),
    database=Database(),
)
