"""
Common Mistakes in Async Patterns.
"""

import asyncio


# MISTAKE 1: Forgetting queue.task_done() inside consumer loops
async def mistake_missing_task_done(queue: asyncio.Queue) -> None:
    # DANGER: If consumer fails to call queue.task_done(), awaiting queue.join() hangs INDEFINITELY!
    pass


if __name__ == "__main__":
    print("Always call queue.task_done() in consumer loops after processing an item retrieved from asyncio.Queue!")
