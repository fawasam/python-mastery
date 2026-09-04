"""
Solutions for Threading Exercises.
"""

import threading

counter = 0


def increment_counter() -> None:
    global counter
    counter += 1


def run_n_threads(n: int, target_func) -> None:
    threads = [threading.Thread(target=target_func) for _ in range(n)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    run_n_threads(5, increment_counter)
    assert counter == 5
    print(f"Spawn N threads exercise passed successfully! Counter = {counter}")
