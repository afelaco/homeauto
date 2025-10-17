from abc import ABC, abstractmethod

import polars as pl

from homeauto.core.api.client import ApiClient
from homeauto.core.dataset.bronze import BronzeDataset
from homeauto.core.endpoint import Endpoint


class Extract(ABC):
    @property
    @abstractmethod
    def api_client(self) -> ApiClient:
        pass

    @property
    @abstractmethod
    def endpoint(self) -> Endpoint:
        pass

    @property
    @abstractmethod
    def dataset(self) -> BronzeDataset:
        pass

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def get_data(self) -> pl.DataFrame:
        pass
