from pydantic import BaseModel, model_serializer


class Game(BaseModel):
    appid: int
    name: str
    playtime_forever: int
    content_descriptorids: list[int] | None = None


class Response(BaseModel):
    game_count: int
    games: list[Game]

    @model_serializer
    def serialize(self) -> list[Game]:
        return self.games


class SteamOwnedGamesApiResponseModel(BaseModel):
    response: Response

    @model_serializer
    def serialize(self) -> Response:
        return self.response
