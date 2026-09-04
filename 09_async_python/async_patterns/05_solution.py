"""
Solutions for Async Patterns Exercises.
"""

import asyncio
from typing import AsyncGenerator


async def async_range_multiplier(start: int, count: int, factor: int) -> AsyncGenerator[int, None]:
    for i in range(count):
        await asyncio.sleep(0.01)
        yield (start + i) * factor


async def main() -> None:
    results: list[int] = []
    async for val in async_range_multiplier(1, 3, 10):
        results.append(val)

    assert results == [10, 20, 30]
    print(f"Async range multiplier exercise results: {results}")


if __name__ == "__main__":
    asyncio.run(main())
