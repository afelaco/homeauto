from pydantic import BaseModel


class HltbSearchApiResponseModel(BaseModel):
    game_name: str
    game_alias: str
    completionist: float
