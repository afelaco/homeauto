from pandera.polars import Column, DataFrameSchema
from polars import Boolean, Int64, List, String, Struct

from homeauto.core.dataset.bronze import BronzeDataset

app_details = BronzeDataset(
    container="steam-store",
    name="app-details",
    schema=DataFrameSchema(
        columns={
            "steam_appid": Column(Int64),
            "name": Column(String),
            "short_description": Column(String),
            "about_the_game": Column(String),
            "detailed_description": Column(String),
            "developers": Column(List(String), nullable=True),
            "publishers": Column(List(String), nullable=True),
            "genres": Column(
                List(
                    Struct(
                        {
                            "id": String,
                            "description": String,
                        }
                    )
                ),
                nullable=True,
            ),
            "categories": Column(
                List(
                    Struct(
                        {
                            "id": Int64,
                            "description": String,
                        }
                    )
                ),
                nullable=True,
            ),
            "metacritic": Column(Int64, nullable=True),
            "is_free": Column(Boolean),
            "price_overview": Column(
                Struct(
                    {
                        "currency": String,
                        "initial": Int64,
                        "final": Int64,
                        "discount_percent": Int64,
                    }
                ),
                nullable=True,
            ),
            "release_date": Column(
                Struct(
                    {
                        "coming_soon": Boolean,
                        "date": String,
                    }
                ),
            ),
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
