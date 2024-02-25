from abc import ABC, abstractmethod

class AbstractAuthCheck(ABC):
    """
    Generalisation of an authorization checker
    """
    @abstractmethod
    def validate(self, **kwargs) -> bool:
        """
        Validates the authorization
        """
        pass

    @abstractmethod
    def getcredentials(self, **kwargs) -> str:
        """
        Returns the credentials
        """
        pass