from pydantic import BaseModel, model_validator
from abc import ABC, abstractmethod


class Request(BaseModel, ABC):
    """
    Generalisation of a request in FastAPI
    """
    @model_validator(mode='after')
    @abstractmethod
    def validate(self) -> 'Request':
        """
        Validates the request
        """
        return self
