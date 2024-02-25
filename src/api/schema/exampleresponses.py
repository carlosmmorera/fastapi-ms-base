from typing_extensions import TypedDict

class HelloWorldResponse(TypedDict):
    hello: str

class ReadUserResponse(TypedDict):
    username: str

class PostExampleResponse(TypedDict):
    input: str
    optinput: int | None
    optinput2: str | None
    username: str

class PostExampleWithParamsResponse(TypedDict):
    input: str
    optinput: int | None
    optinput2: str | None
    intpar: int