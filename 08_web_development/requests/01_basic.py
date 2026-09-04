"""
Basic HTTP Client Requests using httpx Client.
"""

import httpx


def fetch_ip_info() -> dict[str, str] | None:
    # Use httpx.Client with explicit timeout
    with httpx.Client(timeout=5.0) as client:
        try:
            # Public HTTP test endpoint
            response = client.get("https://httpbin.org/get", params={"source": "python_course"})
            response.raise_for_status()
            data = response.json()
            return data.get("args", {})
        except httpx.HTTPError as err:
            print(f"HTTP Request failed: {err}")
            return None


if __name__ == "__main__":
    params = fetch_ip_info()
    if params:
        print(f"Server received query params: {params}")
    else:
        print("Completed client request attempt.")
