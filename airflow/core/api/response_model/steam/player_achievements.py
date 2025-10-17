from pydantic import BaseModel, model_serializer, Field


class Achievement(BaseModel):
    api_name: str = Field(alias="apiname")
    achieved: int
    unlock_time: int = Field(alias="unlocktime")


class PlayerStats(BaseModel):
    steam_id: str = Field(alias="steamID")
    game_name: str = Field(alias="gameName")
    achievements: list[Achievement]


class SteamPlayerAchievementsApiResponseModel(BaseModel):
    player_stats: PlayerStats = Field(alias="playerstats")

    @model_serializer
    def serialize(self) -> PlayerStats:
        return self.player_stats
