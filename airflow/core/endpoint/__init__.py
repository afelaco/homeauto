from abc import ABC
from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class Endpoint(ABC):
    url: str
    response_model: type[BaseModel]
