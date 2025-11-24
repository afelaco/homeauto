from abc import ABC

from pandera.polars import Column, DataFrameSchema

from homeauto.core.infra import Database
from homeauto.core.table import Table


class FactTable(Table, ABC):
    pass


fact_owned_games_tags = FactTable(
    name="fact_owned_games_tags",
    schema=DataFrameSchema(
        columns={
            "id": Column(str),
            "name": Column(str),
            "playtime": Column(int),
            "tag": Column(str, nullable=True),
        },
        strict=True,
    ),
    database=Database(),
)
