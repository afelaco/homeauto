import json
from typing import Any

from howlongtobeatpy import HowLongToBeat
from tqdm import tqdm

from homeauto.core import get_logger
from homeauto.core.endpoint import Endpoint

logger = get_logger(name=__name__)


class HltbApiClient:
    def __init__(self) -> None:
        self.session = HowLongToBeat()

    def get(self, endpoint: Endpoint, params: dict[str, str]) -> list[dict[str, Any]]:
        response = []
        for name in tqdm(params["names"]):
            response.extend([vars(game) for game in self.session.search(game_name=name)])
        data = endpoint.response_model.model_validate_json(json.dumps(response)).model_dump(by_alias=True)

        logger.info("%s records read from %s", len(data))

        return data  # type: ignore
