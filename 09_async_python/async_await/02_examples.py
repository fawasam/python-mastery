"""
Concurrent Coroutine Execution with asyncio.gather().
"""

import asyncio
import time


async def fetch_api_endpoint(endpoint_name: str, delay: float) -> dict[str, str]:
    print(f"[FETCHING] Querying {endpoint_name}...")
    await asyncio.sleep(delay)
    return {"endpoint": endpoint_name, "status": "200 OK"}


async def main() -> None:
    start = time.perf_counter()

    # asyncio.gather schedules all coroutines concurrently on the event loop!
    results = await asyncio.gather(
        fetch_api_endpoint("UserMicroservice", 0.2),
        fetch_api_endpoint("OrderMicroservice", 0.2),
        fetch_api_endpoint("PaymentGateway", 0.2),
    )

    duration = time.perf_counter() - start
    print("\n--- Concurrent API Results ---")
    for res in results:
        print(f" - {res['endpoint']}: {res['status']}")

    print(f"Total concurrent execution time: {duration:.4f}s (vs 0.60s if sequential!)")


if __name__ == "__main__":
    asyncio.run(main())
