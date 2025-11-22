from homeauto.core.api.response_model.steam.owned_games import SteamOwnedGamesApiResponseModel
from homeauto.core.api.response_model.steam.player_achievements import (
    SteamPlayerAchievementsApiResponseModel,
)
from homeauto.core.endpoint import Endpoint


class IPlayerService:
    __SERVICE = "IPlayerService"
    owned_games = Endpoint(
        url=f"{__SERVICE}/GetOwnedGames/v0001/",
        response_model=SteamOwnedGamesApiResponseModel,
    )


class ISteamUserStats:
    __SERVICE = "ISteamUserStats"
    player_achievements = Endpoint(
        url=f"{__SERVICE}/GetPlayerAchievements/v0001/",
        response_model=SteamPlayerAchievementsApiResponseModel,
    )
