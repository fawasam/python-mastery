"""
Topic: Unpacking Solutions
File: 05_solution.py
"""
from typing import Any

def level_1_easy() -> None:
    data = [10, 20, 30, 40, 50]
    first, *middle, last = data
    print(f"First: {first} | Middle: {middle} | Last: {last}")


def level_2_medium() -> dict[str, int]:
    d1 = {"a": 1}
    d2 = {"b": 2}
    d3 = {"c": 3}
    merged = {**d1, **d2, **d3}
    print(f"Merged dict: {merged}")
    return merged


def level_3_hard() -> None:
    records = [("Alice", (90, 85, 95)), ("Bob", (70, 80, 75))]
    for name, (g1, g2, g3) in records:
        avg = (g1 + g2 + g3) / 3
        print(f"Student: {name:<7} | Grades: {g1}, {g2}, {g3} | Avg: {avg:.1f}")


def level_4_real_world(*base_configs: dict[str, Any], **override_kwargs: Any) -> dict[str, Any]:
    merged_config: dict[str, Any] = {}
    for cfg in base_configs:
        merged_config.update(cfg)
    merged_config.update(override_kwargs)
    print(f"Final merged configuration: {merged_config}")
    return merged_config


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium()

    print("\n--- Level 3 ---")
    level_3_hard()

    print("\n--- Level 4 ---")
    cfg1 = {"env": "prod", "port": 8000}
    cfg2 = {"port": 8080, "workers": 4}
    level_4_real_world(cfg1, cfg2, debug=True, port=9000)
