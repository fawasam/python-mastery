"""
Basic Threading Lock to Prevent Race Conditions.
"""

import threading

shared_counter = 0
counter_lock = threading.Lock()


def safe_increment_1000_times() -> None:
    global shared_counter
    for _ in range(1000):
        # Critical section protected by Lock
        with counter_lock:
            shared_counter += 1


def main() -> None:
    threads: list[threading.Thread] = []

    # Spawn 5 concurrent threads incrementing shared_counter
    for _ in range(5):
        t = threading.Thread(target=safe_increment_1000_times)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Guaranteed exact result 5000 due to lock protection!
    assert shared_counter == 5000
    print(f"Final Synchronized Counter Value: {shared_counter} (Exact match guaranteed!)")


if __name__ == "__main__":
    main()
