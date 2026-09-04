"""
Hybrid Concurrency & Parallelism Processing Pipeline.
"""

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time


# 1. I/O-BOUND TASK (Uses ThreadPoolExecutor)
def io_fetch_task(task_id: int) -> dict[str, int | str]:
    time.sleep(0.02)  # Simulate network latency
    return {"id": task_id, "payload": f"RAW_PAYLOAD_{task_id}"}


# 2. CPU-BOUND TASK (Uses ProcessPoolExecutor to bypass GIL)
def cpu_heavy_transform(payload_dict: dict[str, int | str]) -> dict[str, int | str]:
    raw_str = str(payload_dict["payload"])
    # Heavy CPU hashing computation
    computed_hash = hash(raw_str * 1000)
    return {"id": payload_dict["id"], "hash": computed_hash}


def run_hybrid_pipeline(task_ids: list[int]) -> list[dict[str, int | str]]:
    # Step 1: Concurrently fetch data via ThreadPoolExecutor (I/O Bound)
    print(f"--- Step 1: ThreadPool Fetching {len(task_ids)} Items ---")
    with ThreadPoolExecutor(max_workers=4) as thread_pool:
        raw_payloads = list(thread_pool.map(io_fetch_task, task_ids))

    # Step 2: Parallel process transformation via ProcessPoolExecutor (CPU Bound)
    print(f"--- Step 2: ProcessPool CPU Transforming {len(raw_payloads)} Items ---")
    with ProcessPoolExecutor(max_workers=4) as process_pool:
        transformed_records = list(process_pool.map(cpu_heavy_transform, raw_payloads))

    return transformed_records


if __name__ == "__main__":
    items = list(range(1, 9))
    start = time.perf_counter()

    results = run_hybrid_pipeline(items)

    duration = time.perf_counter() - start
    print(f"\nHybrid Pipeline Completed {len(results)} items in {duration:.4f}s")
    assert len(results) == 8
