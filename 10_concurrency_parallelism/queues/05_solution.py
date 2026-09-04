"""
Solutions for Queue Exercises.
"""

import queue
import threading


def process_queue_batch(items: list[str]) -> list[str]:
    q: queue.Queue[str] = queue.Queue()
    results: list[str] = []
    lock = threading.Lock()

    def worker():
        while True:
            item = q.get()
            if item is None:
                q.task_done()
                break
            processed = item.upper()
            with lock:
                results.append(processed)
            q.task_done()

    threads = [threading.Thread(target=worker) for _ in range(2)]
    for t in threads:
        t.start()

    for item in items:
        q.put(item)

    for _ in range(2):
        q.put(None)

    q.join()
    for t in threads:
        t.join()

    return sorted(results)


if __name__ == "__main__":
    out = process_queue_batch(["alpha", "beta", "gamma"])
    assert out == ["ALPHA", "BETA", "GAMMA"]
    print(f"Queue batch processing exercise passed successfully! Output: {out}")
