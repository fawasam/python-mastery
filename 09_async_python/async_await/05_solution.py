"""
Solutions for Async Await Exercises.
"""

import asyncio


async def async_multiply(a: float, b: float, delay: float) -> float:
    await asyncio.sleep(delay)
    return a * b


async def main() -> None:
    res = await async_multiply(4.0, 5.0, 0.05)
    assert res == 20.0
    print(f"Async multiply exercise result: {res}")


if __name__ == "__main__":
    asyncio.run(main())
