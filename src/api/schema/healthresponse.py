from typing import TypedDict

class HealthResponse(TypedDict):
    status: str
    timeUpMs: int
    timeUpHuman: str