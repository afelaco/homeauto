from abc import ABC, abstractmethod

import polars as pl

from homeauto.core.dataset.gold import GoldDataset


class Load(ABC):
    @property
    @abstractmethod
    def output_dataset(self) -> GoldDataset:
        pass

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def get_data(self) -> pl.DataFrame:
        pass
