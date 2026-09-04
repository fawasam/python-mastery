"""
Running CPU-Bound Blocking Functions via loop.run_in_executor().
"""

import asyncio
import time


def blocking_hash_computation(password: str) -> str:
    """Simulates CPU-heavy synchronous computation."""
    time.sleep(0.1)  # Synchronous blocking call
    return f"HASH_{hash(password)}"


async def main() -> None:
    loop = asyncio.get_running_loop()
    start = time.perf_counter()

    # Offload blocking computation to thread pool executor so event loop remains responsive!
    future = loop.run_in_executor(None, blocking_hash_computation, "SecretPassword123")
    result = await future

    duration = time.perf_counter() - start
    print(f"Offloaded CPU Hash Result: {result} (Completed in {duration:.4f}s)")


if __name__ == "__main__":
    asyncio.run(main())
