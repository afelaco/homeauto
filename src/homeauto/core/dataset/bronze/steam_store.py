from pandera.polars import Column, DataFrameSchema

from homeauto.core.dataset.bronze import BronzeDataset

app_details = BronzeDataset(
    container="steam-store",
    name="app-details",
    schema=DataFrameSchema(
        columns={
            "steam_appid": Column(int, nullable=True),
            "metacritic": Column(int, nullable=True),
        },
        strict=True,
    ),
)
