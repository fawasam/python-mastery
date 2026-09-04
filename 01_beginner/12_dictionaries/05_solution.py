"""
Topic: Dictionary Solutions
File: 05_solution.py
"""
from typing import Any

def level_1_easy() -> dict[str, int]:
    inventory = {"apples": 50, "bananas": 30}
    inventory["oranges"] = 40
    inventory["bananas"] = 45
    print(f"Updated inventory: {inventory}")
    return inventory


def level_2_medium(text: str) -> dict[str, int]:
    words = text.split()
    frequency: dict[str, int] = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    print(f"Word frequencies: {frequency}")
    return frequency


def level_3_hard(mapping: dict[str, int]) -> dict[int, list[str]]:
    inverted: dict[int, list[str]] = {}
    for key, val in mapping.items():
        inverted.setdefault(val, []).append(key)
    print(f"Original: {mapping} -> Inverted: {inverted}")
    return inverted


def level_4_real_world(default_config: dict[str, Any], user_override: dict[str, Any]) -> dict[str, Any]:
    merged = default_config.copy()
    for key, val in user_override.items():
        if isinstance(val, dict) and key in merged and isinstance(merged[key], dict):
            merged[key] = level_4_real_world(merged[key], val)
        else:
            merged[key] = val
    print(f"Deep merged config: {merged}")
    return merged


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium("apple banana apple cherry banana apple")

    print("\n--- Level 3 ---")
    level_3_hard({"a": 1, "b": 2, "c": 1})

    print("\n--- Level 4 ---")
    d1 = {"db": {"host": "localhost", "port": 5432}, "debug": False}
    d2 = {"db": {"host": "prod.db"}, "debug": True}
    level_4_real_world(d1, d2)
