from pandera.polars import Column, DataFrameSchema

from homeauto.core.dataset.bronze import BronzeDataset

search = BronzeDataset(
    container="hltb",
    name="search",
    schema=DataFrameSchema(
        columns={
            "game_name": Column(str),
            "similarity": Column(float),
            "completionist": Column(float),
        },
        strict=True,
    ),
)
