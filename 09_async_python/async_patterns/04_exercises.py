"""
Async Patterns Exercises.
"""

import asyncio
from typing import AsyncGenerator


# Exercise 1 (Medium): Async Multiplier Generator
# Write async generator async_range_multiplier(start: int, count: int, factor: int) -> AsyncGenerator[int, None]
# Yields (start + i) * factor with await asyncio.sleep(0.01) delay.
async def async_range_multiplier(start: int, count: int, factor: int) -> AsyncGenerator[int, None]:
    raise NotImplementedError("Implement async_range_multiplier")
