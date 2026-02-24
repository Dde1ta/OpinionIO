import httpx
import asyncio
from General.config import settings


async def send_status_to_db(id: int, status: str):
    # URL with task_id as path parameter
    url = f"{settings.INTERNAL_API_URL}/api/internal/status/{id}"

    # Send status as query parameter
    params = {'status': status}

    # Send the request
    async with httpx.AsyncClient() as client:
        response = await client.post(url, params=params)

    # Raise an error if the request failed
    response.raise_for_status()
    print("Successfully updated status:", response.json())
