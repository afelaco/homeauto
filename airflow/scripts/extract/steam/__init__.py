from abc import ABC

from src.airflow.core.api.client.steam import SteamApiClient
from src.airflow.scripts.extract import Extract


class ExtractSteam(Extract, ABC):
    @property
    def api_client(self) -> SteamApiClient:
        return SteamApiClient()
