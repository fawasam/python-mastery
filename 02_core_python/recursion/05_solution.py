"""
Topic: Recursion Solutions
File: 05_solution.py
"""
from pathlib import Path
from typing import Any

def level_1_easy(n: int) -> int:
    if n <= 1:
        return max(0, n)
    return n + level_1_easy(n - 1)


def level_2_medium(s: str) -> str:
    if len(s) <= 1:
        return s
    return s[-1] + level_2_medium(s[:-1])


def level_3_hard(nested: list[Any]) -> list[Any]:
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(level_3_hard(item))
        else:
            flat.append(item)
    return flat


def level_4_real_world(dir_path: Path, ext: str) -> list[Path]:
    matched = []
    if not dir_path.exists() or not dir_path.is_dir():
        return matched

    for child in dir_path.iterdir():
        if child.is_file() and child.suffix == ext:
            matched.append(child)
        elif child.is_dir():
            matched.extend(level_4_real_world(child, ext))
    return matched


if __name__ == "__main__":
    print("--- Level 1 ---")
    print("Recursive sum 1..10:", level_1_easy(10))

    print("\n--- Level 2 ---")
    print("Reversed 'PYTHON':", level_2_medium("PYTHON"))

    print("\n--- Level 3 ---")
    nested = [1, [2, [3, 4], 5], 6]
    print(f"Flattened {nested} -> {level_3_hard(nested)}")

    print("\n--- Level 4 ---")
    current_dir = Path(__file__).parent
    files = level_4_real_world(current_dir, ".py")
    print(f"Found {len(files)} .py files recursively in topic dir.")
