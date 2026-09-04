"""
Async Worker Queue Engine.
"""

import asyncio
from typing import Callable, Any


class TaskQueueWorker:
    def __init__(self) -> None:
        self.queue: asyncio.Queue[tuple[str, Callable[..., Any], tuple[Any, ...]]] = asyncio.Queue()
        self.results: dict[str, Any] = {}

    async def enqueue(self, task_id: str, func: Callable[..., Any], *args: Any) -> None:
        await self.queue.put((task_id, func, args))

    async def run_worker(self) -> None:
        while not self.queue.empty():
            task_id, func, args = await self.queue.get()
            try:
                res = func(*args)
                self.results[task_id] = {"status": "SUCCESS", "result": res}
            except Exception as err:
                self.results[task_id] = {"status": "FAILED", "error": str(err)}
            finally:
                self.queue.task_done()
