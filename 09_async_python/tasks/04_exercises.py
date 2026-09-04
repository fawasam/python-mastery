"""
Task Exercises.
"""

import asyncio


async def delayed_square(x: int) -> int:
    await asyncio.sleep(0.01)
    return x * x


# Exercise 1 (Medium): Run Parallel Tasks using TaskGroup
# Write run_parallel_squares(values: list[int]) -> list[int]
# Uses TaskGroup (or asyncio.gather) to run delayed_square on all values and return results list.
async def run_parallel_squares(values: list[int]) -> list[int]:
    raise NotImplementedError("Implement run_parallel_squares")
