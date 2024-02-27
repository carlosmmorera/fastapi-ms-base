from dotenv import load_dotenv
import os
# Loads environment variables from a .env file into the current environment
load_dotenv()
# Loads environment variables from a specific .env file based on the value of the "ENV" environment variable For
# example, if "ENV" environment variable is set to "dev", it will load variables from the file
# ".dev.env" in the "envs" directory
load_dotenv(f'envs/.{os.getenv("ENV")}.env')

import uvicorn
from config.api import ConfigAPI
import config.config as config

if __name__ == "__main__":
    apiconfig = config.get('api', ConfigAPI)
    uvicorn.run("app:app", host=apiconfig.host, port=apiconfig.port)