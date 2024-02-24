from ..exceptions.httpexception import UnauthorizedException
from .authchecktypes.abstractauthcheck import AbstractAuthCheck
from typing import Annotated
from fastapi.security import HTTPBasicCredentials
from fastapi import Depends
from .authchecktypes.basicauthcheck import security


class AuthCheck():
    __checker: AbstractAuthCheck

    def __init__(self, checker: AbstractAuthCheck):
        self.__checker = checker

    def check_authorization(self, 
                            credentials: Annotated[HTTPBasicCredentials, Depends(security)]
                            ) -> str:
        if not(self.__checker.validate(credentials=credentials)):
            raise UnauthorizedException('Invalid credentials')
        
        return self.__checker.getcredentials(credentials=credentials)