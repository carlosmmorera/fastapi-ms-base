# fastapi-ms-base
This is an example microservice which can be used as code base for any Python microservice implemented with FastAPI.

## Scripts
You can run your microservice by using the following commands:
- `uvicorn src.app:app --reload`: run the live server using Uvicorn. The `--reload` option consumes much more resources, is more unstable, etc. It helps a lot during development, but you shouldn't use it in production.

## API Documentation
Thanks to FastAPI, if you execute your microservice locally, you can see the interactive API documentatio in the following URLs:
- `http://127.0.0.1:8000/docs`: you will see the automatic interactive API documentation provided by [Swagger UI](https://github.com/swagger-api/swagger-ui).
- `http://127.0.0.1:8000/redoc`: you will see the automatic interactive API documentation provided by [ReDoc](https://github.com/Redocly/redoc).