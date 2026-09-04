"""
Asyncio Exercises.
"""

import asyncio


# Exercise 1 (Medium): Safe Timeout Runner
# Write fetch_with_timeout(coro, timeout_sec: float) -> tuple[bool, Any]
# Awaits asyncio.wait_for(coro, timeout_sec).
# Returns (True, result) on success, or (False, None) if TimeoutError is raised.
async def fetch_with_timeout(coro, timeout_sec: float) -> tuple[bool, object]:
    raise NotImplementedError("Implement fetch_with_timeout")
