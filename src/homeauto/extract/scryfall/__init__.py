from abc import ABC

from homeauto.core.api.client.scryfall import ScryfallApiClient
from homeauto.extract import Extract


class ExtractScryfall(Extract, ABC):
    @property
    def api_client(self) -> ScryfallApiClient:
        return ScryfallApiClient()
