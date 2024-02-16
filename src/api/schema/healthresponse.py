from typing_extensions import TypedDict

class HealthResponse(TypedDict):
    status: str
    timeUpMs: int
    timeUpHuman: str