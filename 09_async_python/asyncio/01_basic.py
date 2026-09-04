"""
Basic asyncio.wait_for Timeout Handling.
"""

import asyncio


async def long_running_query() -> str:
    print("[QUERY] Processing database query...")
    await asyncio.sleep(2.0)  # Takes 2 seconds
    return "Query Data"


async def main() -> None:
    try:
        # Enforce 0.5s timeout on 2.0s query
        print("Enforcing 0.5s timeout limit on query...")
        await asyncio.wait_for(long_running_query(), timeout=0.5)
    except TimeoutError:
        print("[TIMEOUT CAUGHT] Query exceeded maximum allowed 0.5s threshold!")


if __name__ == "__main__":
    asyncio.run(main())
