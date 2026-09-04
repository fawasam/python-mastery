"""
Solutions for Event Loop Exercises.
"""

import asyncio
import time


def sync_heavy_task(val: int) -> int:
    time.sleep(0.02)
    return val * 10


async def run_offloaded_task(val: int) -> int:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, sync_heavy_task, val)


async def main() -> None:
    res = await run_offloaded_task(5)
    assert res == 50
    print(f"Offloaded task exercise result: {res}")


if __name__ == "__main__":
    asyncio.run(main())
