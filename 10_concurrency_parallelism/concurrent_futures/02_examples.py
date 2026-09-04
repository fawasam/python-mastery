"""
Using as_completed() to Process Futures as Results Become Available.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import random
import time


def variable_delay_worker(task_id: int) -> str:
    delay = random.uniform(0.01, 0.08)
    time.sleep(delay)
    return f"Task #{task_id} (delay={delay:.3f}s)"


def main() -> None:
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Submit futures
        futures = [executor.submit(variable_delay_worker, i) for i in range(1, 6)]

        # as_completed yields futures as soon as they finish (out-of-order execution processing!)
        print("Processing Results as Completed:")
        for future in as_completed(futures):
            res = future.result()
            print(f" Finished: {res}")


if __name__ == "__main__":
    main()
