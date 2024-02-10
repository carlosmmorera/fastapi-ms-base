from fastapi import HTTPException

class BadRequestException(HTTPException):
    def __init__(self, extra: any = None):
        super().__init__(status_code=400, detail=f'Bad Request: {extra}' if extra else 'Bad Request')


class InternalServerErrorException(HTTPException):
    def __init__(self, extra: any = None):
        super().__init__(status_code=500, detail=f'Internal Server Error: {extra}' if extra else 'Internal Server Error')


class UnauthorizedException(HTTPException):
    def __init__(self, extra: any = None):
        super().__init__(status_code=401, detail=f'Unauthorized: {extra}' if extra else 'Unauthorized')


class ForbiddenException(HTTPException):
    def __init__(self, extra: any = None):
        super().__init__(status_code=403, detail=f'Forbidden: {extra}' if extra else 'Forbidden')


class NotFoundException(HTTPException):
    def __init__(self, extra: any = None):
        super().__init__(status_code=404, detail=f'Not Found: {extra}' if extra else 'Not Found')


class MethodNotAllowedException(HTTPException):
    def __init__(self, extra: any = None):
        super().__init__(status_code=405, detail=f'Method Not Allowed: {extra}' if extra else 'Method Not Allowed')


class RequestTimeoutException(HTTPException):
    def __init__(self, extra: any = None):
        super().__init__(status_code=408, detail=f'Request Timeout: {extra}' if extra else 'Request Timeout')