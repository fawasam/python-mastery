"""
Common Mistakes with Asyncio Tasks.
"""

import asyncio


# MISTAKE 1: Fire-and-forget tasks without keeping strong references
# In Python 3.11+, background tasks created via create_task() without storing a reference in a variable or set
# can be garbage collected mid-execution!
background_tasks = set()


def mistake_fire_and_forget() -> None:
    # DANGER: asyncio.create_task(worker()) without saving reference risks GC cleanup!
    pass


def good_task_reference() -> None:
    task = asyncio.create_task(asyncio.sleep(0.01))
    background_tasks.add(task)
    task.add_done_callback(background_tasks.discard)


if __name__ == "__main__":
    print("Always keep strong references to background tasks to prevent garbage collection mid-execution!")
