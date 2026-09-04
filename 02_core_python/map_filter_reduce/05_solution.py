"""
Topic: Map, Filter & Reduce Solutions
File: 05_solution.py
"""
from functools import reduce
from typing import Any

def level_1_easy() -> list[float]:
    celsius = [0, 20, 30, 40]
    fahrenheit = list(map(lambda c: round(c * 1.8 + 32, 1), celsius))
    print(f"Celsius: {celsius} -> Fahrenheit: {fahrenheit}")
    return fahrenheit


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def level_2_medium() -> list[int]:
    numbers = list(range(2, 30))
    primes = list(filter(is_prime, numbers))
    print(f"Primes in range(2, 30): {primes}")
    return primes


def level_3_hard(numbers: list[int]) -> int:
    max_val = reduce(lambda a, b: a if a > b else b, numbers)
    print(f"Max in {numbers} using reduce: {max_val}")
    return max_val


def level_4_real_world(logs: list[dict[str, Any]]) -> int:
    success_logs = filter(lambda entry: entry.get("status") == 200, logs)
    response_bytes = map(lambda entry: entry.get("bytes", 0), success_logs)
    total_bytes = reduce(lambda acc, b: acc + b, response_bytes, 0)
    print(f"Total response bytes for HTTP 200: {total_bytes:,} bytes")
    return total_bytes


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium()

    print("\n--- Level 3 ---")
    level_3_hard([14, 88, 42, 99, 12])

    print("\n--- Level 4 ---")
    log_data = [
        {"status": 200, "bytes": 1024},
        {"status": 404, "bytes": 512},
        {"status": 200, "bytes": 4096},
    ]
    level_4_real_world(log_data)
