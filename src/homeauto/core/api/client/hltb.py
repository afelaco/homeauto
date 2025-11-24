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
        data = []
        for name in tqdm(params["names"]):
            data.extend(
                [{key: vars(entry)[key] for key in params["select"]} for entry in self.session.search(game_name=name)]
            )

        logger.info("%s records read from HTLB", len(data))

        return data
