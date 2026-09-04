"""
Inter-Process Communication using multiprocessing.Queue.
"""

import multiprocessing


def process_producer(q: multiprocessing.Queue) -> None:
    for item in ["Data A", "Data B", "Data C"]:
        q.put(item)


def process_consumer(q: multiprocessing.Queue, results: list[str]) -> None:
    while not q.empty():
        item = q.get()
        results.append(item)


if __name__ == "__main__":
    q: multiprocessing.Queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=process_producer, args=(q,))
    p1.start()
    p1.join()

    retrieved = []
    while not q.empty():
        retrieved.append(q.get())

    print(f"Retrieved items from multiprocessing Queue: {retrieved}")
    assert len(retrieved) == 3
