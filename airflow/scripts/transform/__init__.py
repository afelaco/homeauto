from abc import ABC, abstractmethod

import polars as pl

from src.airflow.core.dataset.bronze import BronzeDataset
from src.airflow.core.dataset.silver import SilverDataset


class Transform(ABC):
    @property
    @abstractmethod
    def input_dataset(self) -> BronzeDataset:
        pass

    @property
    @abstractmethod
    def output_dataset(self) -> SilverDataset:
        pass

    @property
    @abstractmethod
    def mapping(self) -> dict[str, str]:
        pass

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def get_data(self) -> pl.DataFrame:
        pass
