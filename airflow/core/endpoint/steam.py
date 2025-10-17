from src.airflow.core.api.response_model.steam.owned_games import SteamOwnedGamesApiResponseModel
from src.airflow.core.api.response_model.steam.player_achievements import (
    SteamPlayerAchievementsApiResponseModel,
)
from src.airflow.core.endpoint import Endpoint


owned_games = Endpoint(
    url="IPlayerService/GetOwnedGames/v1/",
    response_model=SteamOwnedGamesApiResponseModel,
)
player_achievements = Endpoint(
    url="ISteamUserStats/GetPlayerAchievements/v0001/",
    response_model=SteamPlayerAchievementsApiResponseModel,
)
