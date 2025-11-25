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

app_reviews = BronzeDataset(
    container="steam-store",
    name="app-reviews",
    schema=DataFrameSchema(
        columns={
            "app_id": Column(str, unique=True),
            "num_reviews": Column(int),
            "review_score": Column(int),
            "review_score_desc": Column(str),
            "total_positive": Column(int),
            "total_negative": Column(int),
            "total_reviews": Column(int),
        },
        strict=True,
    ),
)
