"""
Common Mistakes with async and await.
"""

import asyncio
import time


async def sample_coroutine() -> str:
    await asyncio.sleep(0.01)
    return "done"


# MISTAKE 1: Calling coroutine without await
async def mistake_forget_await() -> None:
    # DANGER: 'res' becomes a <coroutine object>! The coroutine function DOES NOT EXECUTE!
    res = sample_coroutine()
    # Warning raised: RuntimeWarning: coroutine 'sample_coroutine' was never awaited
    pass


# MISTAKE 2: Using time.sleep() inside async def
async def mistake_blocking_sleep() -> None:
    # DANGER: time.sleep() blocks the OS thread, freezing the event loop for all concurrent tasks!
    # ALWAYS use 'await asyncio.sleep()' instead!
    pass


if __name__ == "__main__":
    print("Always use 'await' when calling coroutine functions, and never use blocking 'time.sleep()' inside async code!")
