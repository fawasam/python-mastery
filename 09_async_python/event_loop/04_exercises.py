"""
Event Loop Exercises.
"""

import asyncio
import time


def sync_heavy_task(val: int) -> int:
    time.sleep(0.02)
    return val * 10


# Exercise 1 (Medium): Offload Heavy Task
# Write async function run_offloaded_task(val: int) -> int
# Uses asyncio.get_running_loop().run_in_executor(None, sync_heavy_task, val) to run task asynchronously.
async def run_offloaded_task(val: int) -> int:
    raise NotImplementedError("Implement run_offloaded_task")
