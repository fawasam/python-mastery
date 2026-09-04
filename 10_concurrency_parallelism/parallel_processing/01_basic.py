"""
Parallel Dataset Chunking with ProcessPoolExecutor.
"""

from concurrent.futures import ProcessPoolExecutor
import time


def process_data_chunk(chunk: list[int]) -> int:
    """Computes sum of squares for a chunk of data."""
    return sum(x * x for x in chunk)


def chunkify(dataset: list[int], chunk_size: int) -> list[list[int]]:
    return [dataset[i : i + chunk_size] for i in range(0, len(dataset), chunk_size)]


def main() -> None:
    data = list(range(1, 100_001))
    chunks = chunkify(data, chunk_size=25_000)

    start = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        chunk_sums = list(executor.map(process_data_chunk, chunks))

    total_sum = sum(chunk_sums)
    duration = time.perf_counter() - start

    print(f"Parallel chunked calculation total: {total_sum} (Completed in {duration:.4f}s)")
    assert total_sum == sum(x * x for x in data)


if __name__ == "__main__":
    main()
