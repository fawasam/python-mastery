"""
Task Queue Main Entrypoint.
"""

import asyncio
from app.worker import TaskQueueWorker


def sample_job(x: int, y: int) -> int:
    return x * y


async def main_async() -> None:
    worker = TaskQueueWorker()
    await worker.enqueue("job_1", sample_job, 5, 10)
    await worker.run_worker()
    print("Worker Results:", worker.results)


if __name__ == "__main__":
    asyncio.run(main_async())
