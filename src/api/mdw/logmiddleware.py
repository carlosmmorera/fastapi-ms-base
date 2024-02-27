from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from loguru import logger
from starlette.routing import Match


# Middleware to log request and responses
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        params_log: str = "Params: " + ",\n".join([f"{name}: {value}" for route in request.app.router.routes
                                                   for match, scope in [route.matches(request)] if match == Match.FULL
                                                   for name, value in scope["path_params"].items()])
        # headers_log: str = "Headers: " + ", ".join([f"{name}: {value}" for name, value in request.headers.items()])
        headers_log: str = "Headers: " + ", ".join([
                                                       f"{name}: {value if name != 'authorization' else value[:len(value) // 2] + '*' * (len(value) - len(value) // 2)}"
                                                       for name, value in request.headers.items()])

        logger.debug(f"{request.method} {request.url}" + "\n" + params_log + "\n" + headers_log)

        response = await call_next(request)
        logger.debug(f"{request.method} {request.url} " + "Status code: " + str(response.status_code))
        return response
