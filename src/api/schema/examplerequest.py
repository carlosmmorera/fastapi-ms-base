from ..exceptions.httpexception import BadRequestException
from .request import Request
from typing import Optional
from loguru import logger


class ExampleRequest(Request):
    input: str
    optinput: int | None = None
    optinput2: Optional[str] = None

    def validate(self) -> 'Request':
        """
        Validates the request
        """
        if len(self.input) < 3:
            logger.error('input field must have at least 3 characters')
            raise BadRequestException('input field must have at least 3 characters')
        return self
