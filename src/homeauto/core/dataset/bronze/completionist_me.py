from pandera.polars import Column, DataFrameSchema

from homeauto.core.dataset.bronze import BronzeDataset

completion_playtime_avg = BronzeDataset(
    container="completionist_me",
    name="completion-playtime-avg",
    schema=DataFrameSchema(
        columns={
            "app_id": Column(int, unique=True),
            "completion_playtime_avg": Column(str),
        },
        strict=True,
    ),
)
