"""
Topic: Scope Solutions
File: 05_solution.py
"""
from typing import Callable

x_global = 10

def level_1_easy() -> None:
    x_local = 20
    print(f"Global x: {x_global} | Local x: {x_local}")


def level_2_medium(initial_value: int = 0) -> Callable[[int], int]:
    total = initial_value

    def add(value: int) -> int:
        nonlocal total
        total += value
        print(f"Accumulated total: {total}")
        return total

    return add


GLOBAL_CONFIG = {"debug": False, "max_connections": 100}

def level_3_hard() -> None:
    # Modifying internal state of a global MUTABLE object does NOT require `global` keyword!
    GLOBAL_CONFIG["debug"] = True
    print("Updated global config dict without reassigning reference:", GLOBAL_CONFIG)


def level_4_real_world(tokens: int, refill_rate: float) -> Callable[[], bool]:
    current_tokens = float(tokens)

    def consume() -> bool:
        nonlocal current_tokens
        if current_tokens >= 1.0:
            current_tokens -= 1.0
            print(f"Token consumed. Remaining: {current_tokens:.1f}")
            return True
        print("Rate limit exceeded! No tokens available.")
        return False

    return consume


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    acc = level_2_medium(10)
    acc(5)
    acc(15)

    print("\n--- Level 3 ---")
    level_3_hard()

    print("\n--- Level 4 ---")
    limiter = level_4_real_world(2, 1.0)
    limiter()
    limiter()
    limiter()
