"""
Basic Async Producer-Consumer Pattern using asyncio.Queue.
"""

import asyncio


async def producer(queue: asyncio.Queue[str], count: int) -> None:
    for i in range(1, count + 1):
        item = f"Job #{i}"
        print(f"[PRODUCER] Enqueuing {item}...")
        await queue.put(item)
        await asyncio.sleep(0.01)


async def consumer(consumer_id: int, queue: asyncio.Queue[str]) -> None:
    while True:
        item = await queue.get()
        print(f" [CONSUMER {consumer_id}] Processing {item}...")
        await asyncio.sleep(0.02)
        queue.task_done()


async def main() -> None:
    queue: asyncio.Queue[str] = asyncio.Queue(maxsize=10)

    # Start 2 worker consumers
    workers = [asyncio.create_task(consumer(i, queue)) for i in (1, 2)]

    # Run producer
    await producer(queue, 4)

    # Wait until all queued items are processed via task_done()
    await queue.join()

    # Cancel background worker loops
    for w in workers:
        w.cancel()

    print("[MAIN] All queue items processed cleanly!")


if __name__ == "__main__":
    asyncio.run(main())
