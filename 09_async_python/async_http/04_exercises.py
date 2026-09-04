"""
Async HTTP Exercises.
"""

from typing import Any
import httpx


# Exercise 1 (Medium): Async Batch Fetcher
# Write async_fetch_all(client: httpx.AsyncClient, urls: list[str]) -> list[dict[str, Any]]
# Uses asyncio.gather to fetch all URLs concurrently and return a list of response.json() results.
async def async_fetch_all(client: httpx.AsyncClient, urls: list[str]) -> list[dict[str, Any]]:
    raise NotImplementedError("Implement async_fetch_all")
