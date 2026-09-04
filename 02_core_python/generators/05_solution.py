"""
Topic: Generator Solutions
File: 05_solution.py
"""
import math
from typing import Any, Generator

def even_generator(limit: int) -> Generator[int, None, None]:
    for i in range(0, limit + 1, 2):
        yield i


def level_1_easy() -> list[int]:
    result = list(even_generator(10))
    print(f"Evens up to 10: {result}")
    return result


def level_2_medium() -> list[float]:
    gen_exp = (math.sqrt(x) for x in range(1, 20) if x % 2 != 0)
    result = [round(v, 2) for v in gen_exp]
    print(f"Square roots of odds (1..20): {result}")
    return result


def infinite_id_generator(prefix: str = "usr_") -> Generator[str, None, None]:
    counter = 1
    while True:
        yield f"{prefix}{counter}"
        counter += 1


def level_3_hard() -> None:
    id_gen = infinite_id_generator("id_")
    sample_ids = [next(id_gen) for _ in range(4)]
    print(f"Generated IDs: {sample_ids}")


def parse_csv_stream(file_lines: list[str]) -> Generator[dict[str, str], None, None]:
    if not file_lines:
        return
    headers = [h.strip() for h in file_lines[0].split(",")]
    for line in file_lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(",")]
        yield dict(zip(headers, values, strict=False))


def level_4_real_world() -> None:
    csv_rows = [
        "name, role, salary",
        "Alice, Developer, 95000",
        "Bob, Manager, 110000",
    ]
    stream = parse_csv_stream(csv_rows)
    print("Parsed CSV Stream:")
    for record in stream:
        print(f"  Record: {record}")


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium()

    print("\n--- Level 3 ---")
    level_3_hard()

    print("\n--- Level 4 ---")
    level_4_real_world()
