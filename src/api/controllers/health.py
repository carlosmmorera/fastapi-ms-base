import time
from humanize import naturaltime
from ..schema.healthresponse import HealthResponse

start_time: float = time.time()
    

class HealthController:
    @staticmethod
    async def get_health() -> HealthResponse:
        timedelta: float = time.time() - start_time
        return {
            'status': 'OK',
            'timeUpMs': int(timedelta * 1000),
            'timeUpHuman': naturaltime(timedelta)
        }