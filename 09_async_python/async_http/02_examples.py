"""
Rate-Limited Async HTTP Fetching with asyncio.Semaphore.
"""

import asyncio
from unittest.mock import MagicMock
import httpx


async def throttled_fetch(sem: asyncio.Semaphore, client: httpx.AsyncClient, url: str) -> dict[str, str]:
    # Acquire semaphore slot to enforce maximum concurrency ceiling
    async with sem:
        response = await client.get(url)
        return response.json()


async def main() -> None:
    # Restrict maximum simultaneous outbound HTTP connections to 2
    sem = asyncio.Semaphore(2)

    # Use mock client for test verification
    mock_client = MagicMock(spec=httpx.AsyncClient)
    mock_response = MagicMock()
    mock_response.json.return_value = {"status": "ok"}

    async def mock_get(url: str):
        await asyncio.sleep(0.01)
        return mock_response

    mock_client.get = mock_get

    urls = [f"https://api.dev.io/item/{i}" for i in range(5)]
    tasks = [throttled_fetch(sem, mock_client, url) for url in urls]
    results = await asyncio.gather(*tasks)

    assert len(results) == 5
    print(f"Rate-limited async HTTP batch completed {len(results)} requests successfully!")


if __name__ == "__main__":
    asyncio.run(main())
