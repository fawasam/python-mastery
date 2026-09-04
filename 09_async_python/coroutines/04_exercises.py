"""
Coroutine Exercises.
"""

import inspect


async def dummy_async_task() -> None:
    pass


# Exercise 1 (Easy): Coroutine State Verification
# Write check_is_coroutine_created(coro) -> bool
# Returns True if inspect.getcoroutinestate(coro) == inspect.CORO_CREATED.
def check_is_coroutine_created(coro) -> bool:
    raise NotImplementedError("Implement check_is_coroutine_created")
