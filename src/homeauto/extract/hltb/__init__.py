from homeauto.core.api.client.hltb import HltbApiClient


class ExtractHltb:
    @property
    def api_client(self) -> HltbApiClient:
        return HltbApiClient()
