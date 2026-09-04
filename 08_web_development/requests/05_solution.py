"""
Solutions for HTTP Requests Exercises.
"""

from unittest.mock import MagicMock
import httpx


def safe_fetch_json(client: httpx.Client, url: str) -> dict | None:
    try:
        response = client.get(url, timeout=5.0)
        response.raise_for_status()
        return response.json()
    except (httpx.HTTPError, Exception):
        return None


if __name__ == "__main__":
    # Test using mock httpx.Client
    mock_client = MagicMock(spec=httpx.Client)
    mock_response = MagicMock()
    mock_response.json.return_value = {"status": "ok"}
    mock_client.get.return_value = mock_response

    data = safe_fetch_json(mock_client, "https://api.dev.io/health")
    assert data == {"status": "ok"}
    print("Safe fetch JSON exercise passed with mock client successfully!")
