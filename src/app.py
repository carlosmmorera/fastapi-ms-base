from fastapi import FastAPI, status
from .api.routers import example, configuration
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

print('Starting app...')
print('Loading general environment...')
load_dotenv()
print(f'Loading {os.getenv("ENV")} environment')
load_dotenv(f'envs/.{os.getenv("ENV")}.env')

from .config import config

app = FastAPI()

print(f'Example of config usage: {config.get("api")}')
print(f'Example of config usage: {config.get("postgresql")}')

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


app.include_router(configuration.router, prefix="/config",
    tags=["configuration"])

app.include_router(example.router, prefix="/example",
    tags=["example"])

