"""
Tests for Task Queue Worker.
"""

import asyncio
from app.worker import TaskQueueWorker


def test_task_queue_worker() -> None:
    async def _async_test() -> None:
        worker = TaskQueueWorker()
        await worker.enqueue("job_test", lambda a, b: a + b, 10, 20)
        await worker.run_worker()

        assert "job_test" in worker.results
        assert worker.results["job_test"]["result"] == 30

    asyncio.run(_async_test())
