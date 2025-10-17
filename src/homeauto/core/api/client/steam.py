from typing import Any

from homeauto.core.api.authentication.api_key import ApiKeyAuthentication
from homeauto.core.api.client import ApiClient
from homeauto.core.endpoint import Endpoint
from homeauto.core.logger import get_logger
from homeauto.core.utils import get_secret

logger = get_logger(name=__name__)


class SteamApiClient(ApiClient, ApiKeyAuthentication):
    def __init__(self) -> None:
        self.steam_id = get_secret("STEAM-ID")
        super().__init__(
            base_url="https://api.steampowered.com",
            api_key=get_secret("STEAM-API-KEY"),
        )

    def get_url(self, endpoint: Endpoint) -> str:
        return f"{self.base_url}/{endpoint.url}"

    def get(self, endpoint: Endpoint, params: dict[str, str]) -> list[dict[str, Any]]:
        params = params | {"steamid": self.steam_id}
        response = self.session.get(
            url=self.get_url(endpoint=endpoint),
            params=params,
            headers=self.get_auth_headers(),
        )
        response.raise_for_status()
        data = endpoint.response_model.model_validate_json(response.content).model_dump(by_alias=True)

        logger.info("%s records read from %s", len(data), response.url)

        return [data]

    def get_auth_headers(self) -> dict[str, str]:
        return {"x-webapi-key": self.api_key}
