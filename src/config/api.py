from .version import ConfigVersion

DEFAULT_PORT: int = 8080
DEFAULT_TIMEOUT: int = 1000

class ConfigAPI():
    version: ConfigVersion
    port: int
    timeout: int
    security: dict[str, str]

    def __init__(self,  version: dict = {}, port: int = DEFAULT_PORT, timeout: int = DEFAULT_TIMEOUT,
                 security: dict[str, str] = {}):
        self.version = ConfigVersion(**version)
        self.port = port
        self.timeout = timeout
        self.security = security