"""
Solutions for Parallel Processing Exercises.
"""


def chunk_list(data: list[int], num_chunks: int) -> list[list[int]]:
    if num_chunks <= 0:
        return [data]
    k, m = divmod(len(data), num_chunks)
    return [data[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)] for i in range(num_chunks)]


if __name__ == "__main__":
    chunks = chunk_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], num_chunks=3)
    assert len(chunks) == 3
    assert sum(len(c) for c in chunks) == 10
    print(f"Chunk list exercise solution passed! Created 3 chunks: {chunks}")
