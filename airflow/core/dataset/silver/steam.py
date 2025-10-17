from pandera.polars import DataFrameSchema, Column

from src.airflow.core.dataset.silver import SilverDataset

owned_games = SilverDataset(
    container="steam",
    name="owned-games",
    schema=DataFrameSchema(
        columns={
            "id": Column(str),
            "name": Column(str),
            "playtime": Column(int),
            "tag": Column(str, nullable=True),
        },
        strict=True,
    ),
)
