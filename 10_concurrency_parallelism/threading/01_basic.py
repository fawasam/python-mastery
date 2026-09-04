"""
Basic Multithreading with threading.Thread.
"""

import threading
import time


def download_file_simulation(file_id: int, duration: float) -> None:
    print(f"[THREAD {file_id}] Downloading file {file_id}...")
    time.sleep(duration)  # Releases GIL during I/O wait!
    print(f"[THREAD {file_id}] Completed download of file {file_id}.")


def main() -> None:
    start = time.perf_counter()
    threads: list[threading.Thread] = []

    # Spawn 3 concurrent I/O threads
    for i in range(1, 4):
        t = threading.Thread(target=download_file_simulation, args=(i, 0.1))
        threads.append(t)
        t.start()

    # Join threads to wait for completion
    for t in threads:
        t.join()

    total_time = time.perf_counter() - start
    print(f"All downloads finished in {total_time:.4f}s (Concurrent I/O speedup!)")


if __name__ == "__main__":
    main()
