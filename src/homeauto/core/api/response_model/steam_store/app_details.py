from pydantic import BaseModel, Field, model_serializer


class Metacritic(BaseModel):
    score: int

    @model_serializer
    def serializer(self) -> int:
        return self.score


class Data(BaseModel):
    name: str
    metacritic: Metacritic


class Response(BaseModel):
    data: Data

    @model_serializer
    def serialize(self) -> Data:
        return self.data


class SteamStoreAppDetailsApiResponseModel(BaseModel):
    app_id: Response = Field(alias="placeholder")

    @model_serializer
    def serialize(self) -> Response:
        return self.app_id
