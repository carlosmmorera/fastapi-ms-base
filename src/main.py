import uvicorn
from config.api import ConfigAPI
import config.config as config

if __name__ == "__main__":
    apiconfig = config.get('api', ConfigAPI)
    uvicorn.run("app:app", host=apiconfig.host, port=apiconfig.port)