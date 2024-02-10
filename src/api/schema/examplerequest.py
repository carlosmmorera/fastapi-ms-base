from ..exceptions.httpexception import BadRequestException
from .request import Request
from typing import Optional

class ExampleRequest(Request):
    input: str
    optinput: int | None = None
    optinput2: Optional[str] = None

    def validate(self) -> 'Request':
        """
        Validates the request
        """
        if len(self.input) < 3:
            raise BadRequestException('input field must have at least 3 characters')
        return self