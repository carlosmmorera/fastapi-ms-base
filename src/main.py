import uvicorn
from config.api import ConfigAPI
from config import config

if __name__ == "__main__":
    apiconfig = config.get('api', ConfigAPI)
    uvicorn.run("app:app", host=apiconfig.host, port=apiconfig.port)