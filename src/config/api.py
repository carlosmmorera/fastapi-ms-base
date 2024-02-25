from .version import ConfigVersion

DEFAULT_PORT: int = 8080
DEFAULT_TIMEOUT: int = 1000
DEFAULT_HOST: str = 'localhost'

class ConfigAPI():
    version: ConfigVersion
    port: int
    host: str
    timeout: int
    security: dict[str, str]

    def __init__(self,  version: dict = {}, port: int = DEFAULT_PORT, host: str = DEFAULT_HOST,
                 timeout: int = DEFAULT_TIMEOUT, security: dict[str, str] = {}):
        self.version = ConfigVersion(**version)
        self.port = port
        self.host = host
        self.timeout = timeout
        self.security = security