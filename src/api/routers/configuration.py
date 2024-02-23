from fastapi import APIRouter
from ..controllers.health import HealthController
from ..schema.healthresponse import HealthResponse
from loguru import logger

router = APIRouter()

@router.get("/health")
async def get_health() -> HealthResponse:
    logger.info("Example log in get_health")
    return await HealthController.get_health()