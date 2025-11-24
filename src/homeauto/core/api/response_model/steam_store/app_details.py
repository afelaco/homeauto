from typing import Dict

from pydantic import BaseModel, RootModel, model_serializer


class Metacritic(BaseModel):
    score: int

    @model_serializer
    def serializer(self) -> int:
        return self.score


class Data(BaseModel):
    name: str
    metacritic: Metacritic | None = None


class Response(BaseModel):
    data: Data

    @model_serializer
    def serialize(self) -> Data:
        return self.data


class SteamStoreAppDetailsApiResponseModel(RootModel[Dict[str, Response]]):
    @property
    def app_id(self) -> Response:
        return next(iter(self.root.values()))

    @model_serializer
    def serialize(self) -> Response:
        return self.app_id
