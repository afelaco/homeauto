from pandera.polars import Column, DataFrameSchema

from homeauto.core.dataset.bronze import BronzeDataset

app_details = BronzeDataset(
    container="steam",
    name="app-details",
    schema=DataFrameSchema(
        columns={
            "appid": Column(int, unique=True),
            "name": Column(str),
            "playtime_forever": Column(int),
            "content_descriptorids": Column(list[int], nullable=True),
        },
        strict=True,
    ),
)
