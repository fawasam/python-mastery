"""
Basic Thread-Safe Queue Producer-Consumer Pattern.
"""

import queue
import threading
import time


def worker_consumer(q: queue.Queue) -> None:
    while True:
        item = q.get()
        if item is None:  # Sentinel value indicating shutdown
            q.task_done()
            break
        print(f"[THREAD WORKER] Processing {item}...")
        time.sleep(0.02)
        q.task_done()


def main() -> None:
    task_queue: queue.Queue = queue.Queue(maxsize=5)

    # Launch worker thread
    worker_thread = threading.Thread(target=worker_consumer, args=(task_queue,))
    worker_thread.start()

    # Enqueue work
    for i in range(1, 4):
        task_queue.put(f"Task #{i}")

    # Enqueue sentinel shutdown signal
    task_queue.put(None)

    # Wait for queue items to complete
    task_queue.join()
    worker_thread.join()

    print("Thread-safe queue tasks processed successfully!")


if __name__ == "__main__":
    main()
