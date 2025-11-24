from abc import ABC

from pandera.polars import Column, DataFrameSchema

from homeauto.core.infra import Database
from homeauto.core.table import Table


class DimensionTable(Table, ABC):
    pass


dim_owned_games = DimensionTable(
    name="dim_owned_games",
    schema=DataFrameSchema(
        columns={
            "id": Column(str, unique=True),
            "name": Column(str),
            "playtime": Column(int),
        },
        strict=True,
    ),
    database=Database(),
)
