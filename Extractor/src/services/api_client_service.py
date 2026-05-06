import httpx
from typing import Dict, Any


class APIClient:

    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    async def send_data(self, data: Dict[str, Any]) -> None:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(self.endpoint, json=data)
            response.raise_for_status()
            