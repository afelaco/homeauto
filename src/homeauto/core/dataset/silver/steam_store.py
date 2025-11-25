from pandera.polars import Column, DataFrameSchema

from homeauto.core.dataset.silver import SilverDataset

app_details = SilverDataset(
    container="steam-store",
    name="app-details",
    schema=DataFrameSchema(
        columns={
            "app_id": Column(str, unique=True),
            "score": Column(int),
        },
        strict=True,
    ),
)
