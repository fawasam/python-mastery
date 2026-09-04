"""
Async Generator (`async def` with `yield`) and `async for` Stream Processing.
"""

import asyncio
from typing import AsyncGenerator


async def async_data_stream(limit: int) -> AsyncGenerator[dict[str, int], None]:
    for i in range(1, limit + 1):
        await asyncio.sleep(0.02)
        # Yield dictionary records asynchronously over time
        yield {"sequence_id": i, "payload": i * 100}


async def main() -> None:
    print("--- Consuming Async Generator Stream ---")
    async for record in async_data_stream(3):
        print(f" Received Record #{record['sequence_id']}: Payload = {record['payload']}")


if __name__ == "__main__":
    asyncio.run(main())
