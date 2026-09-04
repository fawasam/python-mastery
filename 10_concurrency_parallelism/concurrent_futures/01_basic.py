"""
Basic ThreadPoolExecutor Usage with executor.map().
"""

from concurrent.futures import ThreadPoolExecutor
import time


def simulate_io_fetch(item_id: int) -> dict[str, int]:
    time.sleep(0.05)  # Simulate I/O latency
    return {"item_id": item_id, "status": 200}


def main() -> None:
    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(simulate_io_fetch, range(1, 6)))

    duration = time.perf_counter() - start
    print(f"Retrieved {len(results)} items in {duration:.4f}s using ThreadPoolExecutor:")
    for r in results:
        print(f" - {r}")


if __name__ == "__main__":
    main()
