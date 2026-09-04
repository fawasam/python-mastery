"""
Solutions for Async HTTP Exercises.
"""

import asyncio
from typing import Any
from unittest.mock import MagicMock
import httpx


async def fetch_one(client: httpx.AsyncClient, url: str) -> dict[str, Any]:
    res = await client.get(url)
    return res.json()


async def async_fetch_all(client: httpx.AsyncClient, urls: list[str]) -> list[dict[str, Any]]:
    tasks = [fetch_one(client, url) for url in urls]
    return list(await asyncio.gather(*tasks))


async def main() -> None:
    mock_client = MagicMock(spec=httpx.AsyncClient)
    mock_response = MagicMock()
    mock_response.json.return_value = {"status": "ok"}

    async def mock_get(url: str):
        await asyncio.sleep(0.01)
        return mock_response

    mock_client.get = mock_get

    results = await async_fetch_all(mock_client, ["http://api.dev/1", "http://api.dev/2"])
    assert len(results) == 2
    assert results[0] == {"status": "ok"}
    print("Async HTTP batch fetcher exercise passed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
