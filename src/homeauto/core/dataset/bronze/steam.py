from pandera.polars import Column, DataFrameSchema

from homeauto.core.dataset.bronze import BronzeDataset

owned_games = BronzeDataset(
    container="steam",
    name="owned-games",
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
player_achievements = BronzeDataset(
    container="steam",
    name="player-achievements",
    schema=DataFrameSchema(
        columns={
            "steamID": Column(int, unique=True),
            "gameName": Column(str),
            "achievements": Column(list[object]),
        },
        strict=True,
    ),
)
