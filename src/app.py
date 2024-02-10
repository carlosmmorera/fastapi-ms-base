from fastapi import FastAPI, status
from .api.routers import example, configuration
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()

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

