"""
Basic Asynchronous HTTP Requests with httpx.AsyncClient.
"""

import asyncio
import httpx


async def fetch_endpoint(client: httpx.AsyncClient, item_id: int) -> dict[str, str] | None:
    try:
        response = await client.get("https://httpbin.org/get", params={"item_id": item_id})
        response.raise_for_status()
        data = response.json()
        return data.get("args", {})
    except httpx.HTTPError as err:
        print(f"Async HTTP request for item {item_id} failed: {err}")
        return None


async def main() -> None:
    async with httpx.AsyncClient(timeout=5.0) as client:
        # Fetch 3 requests concurrently
        tasks = [fetch_endpoint(client, i) for i in range(1, 4)]
        results = await asyncio.gather(*tasks)

        print("\n--- Concurrent Async HTTP Results ---")
        for res in results:
            print(f" Received response args: {res}")


if __name__ == "__main__":
    asyncio.run(main())
