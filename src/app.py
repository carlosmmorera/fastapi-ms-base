import sys
import uvicorn
from fastapi import FastAPI, status
from api.routers import example, configuration
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os
from loguru import logger
from config import config
from config.api import ConfigAPI

if __name__ == "__main__":
    apiconfig: ConfigAPI = config.get('api', ConfigAPI)
    uvicorn.run("app:app", host=apiconfig.host, port=apiconfig.port)

app = FastAPI()

logger.info('Starting app...')
logger.info('Loading general environment...')
# Loads environment variables from a .env file into the current environment
load_dotenv()
# Loads environment variables from a specific .env file based on the value of the "ENV" environment variable For
# example, if "ENV" environment variable is set to "dev", it will load variables from the file
# ".dev.env" in the "envs" directory
logger.info(f'Loading {os.getenv("ENV")} environment...')
load_dotenv(f'envs/.{os.getenv("ENV")}.env')

logger.remove()
logger.add(sys.stderr, level=os.getenv("LOGGING_LEVEL", 'DEBUG'))

# Aggregate middleware to application
# app.add_middleware(LoggingMiddleware)

# this log examples should be deleted
logger.info("This is an info message.")
logger.debug("This is a debug message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical('This is a critical message.')
# log examples end

logger.info('Application started')

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


# @app.middleware("http")
# async def log_middle(request: Request, call_next):
#     params_log = "Params: " + ",\n".join([f"{name}: {value}" for route in request.app.router.routes
#                                           for match, scope in [route.matches(request)] if match == Match.FULL
#                                           for name, value in scope["path_params"].items()])
#     headers_log = "Headers: " + ", ".join([f"{name}: {value}" for name, value in request.headers.items()])
#
#     logger.debug(f"{request.method} {request.url}" + "\n" + params_log + "\n" + headers_log)
#
#     response = await call_next(request)
#     logger.debug(f"{request.method} {request.url} " + str(response.status_code))
#     return response


app.include_router(configuration.router, prefix="/config",
                   tags=["configuration"])

app.include_router(example.router, prefix="/example",
                   tags=["example"])
