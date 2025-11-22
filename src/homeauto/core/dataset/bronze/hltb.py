from pandera.polars import Column, DataFrameSchema

from homeauto.core.dataset.bronze import BronzeDataset

search = BronzeDataset(
    container="hltb",
    name="search",
    schema=DataFrameSchema(
        columns={
            "game_name": Column(str),
            "game_alias": Column(str),
            "completionist": Column(float),
        },
        strict=True,
    ),
)
