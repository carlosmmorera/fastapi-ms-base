import sys
from fastapi import FastAPI, status
from starlette.requests import Request

from api.routers import example, configuration
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import os
from loguru import logger
from api.mdw.logmiddleware import LoggingMiddleware

app = FastAPI()

logger.info('Starting app...')

logger.remove()
logger.add(sys.stderr, level=os.getenv("LOGGING_LEVEL", 'DEBUG'))

# Aggregate middleware to application
app.add_middleware(LoggingMiddleware)

# this log examples should be deleted
logger.info("This is an info message.")
logger.debug("This is a debug message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical('This is a critical message.')
# log examples end

logger.info('Application started')


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


app.include_router(configuration.router, prefix="/config",
                   tags=["configuration"])

app.include_router(example.router, prefix="/example",
                   tags=["example"])
