"""
Solutions for Coroutine Exercises.
"""

import asyncio
import inspect


async def dummy_async_task() -> None:
    pass


def check_is_coroutine_created(coro) -> bool:
    return inspect.getcoroutinestate(coro) == inspect.CORO_CREATED


if __name__ == "__main__":
    c = dummy_async_task()
    assert check_is_coroutine_created(c) is True
    asyncio.run(c)
    assert check_is_coroutine_created(c) is False
    print("Coroutine state verification exercise passed successfully!")
