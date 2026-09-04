"""
Thread-Safe PriorityQueue Example.
"""

import queue
from dataclasses import dataclass, field


@dataclass(order=True)
class PrioritizedJob:
    priority: int
    name: str = field(compare=False)


def demo_priority_queue() -> None:
    pq: queue.PriorityQueue[PrioritizedJob] = queue.PriorityQueue()

    # Enqueue items with different priority numbers (Lower integer = Higher priority)
    pq.put(PrioritizedJob(priority=3, name="Low Priority Batch Export"))
    pq.put(PrioritizedJob(priority=1, name="CRITICAL System Alert"))
    pq.put(PrioritizedJob(priority=2, name="Medium Priority User Request"))

    print("Retrieving Items from PriorityQueue (Sorted by Priority):")
    while not pq.empty():
        job = pq.get()
        print(f" - [Priority {job.priority}] {job.name}")


if __name__ == "__main__":
    demo_priority_queue()
