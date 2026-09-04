"""
Common Mistakes in Queue Synchronization.
"""

import queue


# MISTAKE 1: Forgetting task_done() in queue consumers
def mistake_missing_task_done() -> None:
    q = queue.Queue()
    q.put("Item 1")
    item = q.get()
    # DANGER: Forgetting q.task_done() causes q.join() to block FOREVER because unfinished task count stays at 1!
    pass


if __name__ == "__main__":
    print("Always call q.task_done() after processing an item retrieved with q.get() in multithreaded queues!")
