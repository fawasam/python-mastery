"""
Basic Coroutines and async/await Execution.
"""

import asyncio
import time


async def async_worker(worker_id: int, delay: float) -> str:
    print(f"[WORKER {worker_id}] Started task (sleeping {delay}s)...")
    # Non-blocking pause: yields execution back to event loop!
    await asyncio.sleep(delay)
    print(f"[WORKER {worker_id}] Task completed!")
    return f"Result {worker_id}"


async def main() -> None:
    start = time.perf_counter()

    # Sequential await execution
    res1 = await async_worker(1, 0.1)
    res2 = await async_worker(2, 0.1)

    duration = time.perf_counter() - start
    print(f"Results: {res1}, {res2}")
    print(f"Sequential async duration: {duration:.4f}s")


if __name__ == "__main__":
    asyncio.run(main())
