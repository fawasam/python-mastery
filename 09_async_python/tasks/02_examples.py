"""
Structured Concurrency using asyncio.TaskGroup (Python 3.11+).
"""

import asyncio


async def compute_subtask(name: str, val: int) -> int:
    await asyncio.sleep(0.05)
    return val * 2


async def main() -> None:
    # TaskGroup manages clean lifecycle & error propagation for all sub-tasks
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(compute_subtask("Task A", 10))
        t2 = tg.create_task(compute_subtask("Task B", 20))

    # All tasks are guaranteed complete upon exiting the TaskGroup context block!
    print(f"Task 1 result: {t1.result()}")
    print(f"Task 2 result: {t2.result()}")
    assert t1.result() == 20
    assert t2.result() == 40


if __name__ == "__main__":
    asyncio.run(main())
