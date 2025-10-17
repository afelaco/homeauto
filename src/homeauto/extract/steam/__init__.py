from abc import ABC

from homeauto.core.api.client.steam import SteamApiClient
from homeauto.extract import Extract


class ExtractSteam(Extract, ABC):
    @property
    def api_client(self) -> SteamApiClient:
        return SteamApiClient()
