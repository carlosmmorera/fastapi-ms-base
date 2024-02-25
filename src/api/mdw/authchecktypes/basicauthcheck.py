from .abstractauthcheck import AbstractAuthCheck
import secrets
from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
from ...exceptions.httpexception import UnauthorizedException
from config import config
from config.api import ConfigAPI

security = HTTPBasic()

class BasicAuthCheck(AbstractAuthCheck):
    __valid_credentials: dict[str, str]

    def __init__(self):
        self.__valid_credentials = config.get('api', ConfigAPI).security

    def validate(self, **kwargs) -> bool:
        """
        Validates the authorization
        """
        if 'credentials' not in kwargs:
            raise UnauthorizedException('Credentials not found')
        
        credentials: Annotated[HTTPBasicCredentials, Depends(security)] = kwargs['credentials']

        return (credentials.username in self.__valid_credentials and 
                secrets.compare_digest(credentials.password.encode("utf8"),
                                       self.__valid_credentials[credentials.username].encode("utf8")))
    
    def getcredentials(self, **kwargs) -> str:
        """
        Returns the credentials
        """
        credentials: Annotated[HTTPBasicCredentials, Depends(security)] = kwargs['credentials']
        return credentials.username