from fastapi import APIRouter
from ..controllers.health import HealthController
from ..schema.healthresponse import HealthResponse

router = APIRouter()

@router.get("/health")
async def get_health() -> HealthResponse:
    return await HealthController.get_health()