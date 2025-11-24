from pandera.polars import Column, DataFrameSchema

from homeauto.core.dataset.bronze import BronzeDataset

steam_app = BronzeDataset(
    container="completionist_me",
    name="steam-app",
    schema=DataFrameSchema(
        columns={
            "app_id": Column(int, unique=True),
            "completion_playtime_avg": Column(str),
        },
        strict=True,
    ),
)
