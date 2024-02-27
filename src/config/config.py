from typing import Any, TypeVar
import json
from threading import Lock
import os
from collections.abc import Callable

EXEC_ENV_VAR = "ENV"
CONFIG_PATH_VAR = "CONFIG_PATH"
DEF_CONFIG_PATH = "config/"

class Singleton(type):
    _instances = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
        
class ConfigParser(metaclass=Singleton):
    json_default = {}
    json_env = {}

    def __init__(self) -> None:
        config_path = os.getenv(CONFIG_PATH_VAR) if os.getenv(CONFIG_PATH_VAR) else DEF_CONFIG_PATH
        with open(f'{config_path}/default.json') as f:
            self.json_default = json.load(f)

        if os.getenv(EXEC_ENV_VAR):
            with open(f'{config_path}/{os.getenv(EXEC_ENV_VAR)}.json') as f:
                self.json_env = json.load(f)

    def get(self, key: str) -> Any:
        if key in self.json_env:
            if key not in self.json_default or not(isinstance(self.json_default[key], dict)):
                return self.json_env[key]
            return (self.json_default[key] | self.json_env[key])
        return self.json_default[key]
    
__config_parser = ConfigParser()
        

T = TypeVar('T')
def get(field: str, constructor: Callable[[], T] | None = None) -> T | Any:
    value: Any = __config_parser.get(field)
    if constructor and isinstance(value, dict):
        value = constructor(**value)
    return value