from fastapi import APIRouter, Depends
from ..schema.examplerequest import ExampleRequest
from ..schema.exampleresponses import (
    HelloWorldResponse, 
    ReadUserResponse, 
    PostExampleResponse, 
    PostExampleWithParamsResponse
    )
from ..mdw.authcheck import AuthCheck
from ..mdw.authchecktypes.basicauthcheck import BasicAuthCheck
from typing import Annotated

router: APIRouter = APIRouter()
authchecker: AuthCheck = AuthCheck(BasicAuthCheck())

@router.get("/")
async def hello_world() -> HelloWorldResponse:
    response: HelloWorldResponse = {"hello": "World"}
    return response


# Declare fixed paths first
@router.get("/me")
async def read_user_me() -> ReadUserResponse:
    return {"username": "fakecurrentuser"}


@router.get("/{username}")
async def read_user(username: str) -> ReadUserResponse:
    return {"username": username}


@router.post("/post")
async def post_example(request: ExampleRequest, 
                       username: Annotated[str, Depends(authchecker.check_authorization)]) -> PostExampleResponse:
    return {'input': request.input, 'optinput': request.optinput, 'optinput2': request.optinput2,
            'username': username}


@router.post("/postwithparams/{intpar}")
async def post_with_params_example(intpar: int, request: ExampleRequest) -> PostExampleWithParamsResponse:
    return {'input': request.input, 'optinput': request.optinput, 'optinput2': request.optinput2, 'intpar': intpar}