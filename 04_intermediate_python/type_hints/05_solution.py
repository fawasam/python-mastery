"""
Topic: Type Hints Solutions
File: 05_solution.py
"""
from typing import Any

def level_1_easy(a: float, b: float) -> float:
    return a * b


def level_2_medium(val: int | str) -> int:
    return int(val)


def level_3_hard(matrix: list[list[int]]) -> list[int]:
    return [item for row in matrix for item in row]


def level_4_real_world(env: str, overrides: dict[str, str | int] | None = None) -> dict[str, Any]:
    base_config: dict[str, Any] = {"env": env, "port": 8080}
    if overrides:
        base_config.update(overrides)
    print(f"Loaded config: {base_config}")
    return base_config


if __name__ == "__main__":
    print("--- Level 1 ---")
    print(f"5 * 4 = {level_1_easy(5.0, 4.0)}")

    print("\n--- Level 2 ---")
    print(f"Parsed ID: {level_2_medium('1001')}")

    print("\n--- Level 3 ---")
    print(f"Flattened: {level_3_hard([[1, 2], [3, 4]])}")

    print("\n--- Level 4 ---")
    level_4_real_world("production", {"port": 9090})
