"""
HTTP Requests Exercises.
"""

from unittest.mock import MagicMock
import httpx


# Exercise 1 (Medium): Safe Client Fetch
# Write safe_fetch_json(client: httpx.Client, url: str) -> dict | None
# Executes client.get(url, timeout=5.0).
# Returns response.json() if 200 OK, otherwise returns None on HTTP error or exception.
def safe_fetch_json(client: httpx.Client, url: str) -> dict | None:
    raise NotImplementedError("Implement safe_fetch_json")
