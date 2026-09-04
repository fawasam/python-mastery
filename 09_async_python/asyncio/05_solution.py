"""
Solutions for Asyncio Exercises.
"""

import asyncio
from typing import Any, Coroutine


async def fetch_with_timeout(coro: Coroutine[Any, Any, Any], timeout_sec: float) -> tuple[bool, Any]:
    try:
        res = await asyncio.wait_for(coro, timeout=timeout_sec)
        return True, res
    except TimeoutError:
        return False, None


async def quick_task() -> str:
    await asyncio.sleep(0.01)
    return "fast_result"


async def slow_task() -> str:
    await asyncio.sleep(1.0)
    return "slow_result"


async def main() -> None:
    ok1, val1 = await fetch_with_timeout(quick_task(), 0.1)
    assert ok1 is True and val1 == "fast_result"

    ok2, val2 = await fetch_with_timeout(slow_task(), 0.05)
    assert ok2 is False and val2 is None
    print("Asyncio timeout runner exercise passed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
