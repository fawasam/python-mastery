"""
Topic: Data Types Solutions
File: 05_solution.py
"""
from typing import Any

def level_1_easy() -> None:
    price_str = "49.99"
    total_cost = float(price_str) * 2
    print(f"Total cost: {total_cost:.2f}")


def level_2_medium(val: Any) -> None:
    evaluation = bool(val)
    print(f"Value: {repr(val):<12} -> Truthy: {evaluation}")


def level_3_hard(input_val: str) -> int | None:
    try:
        return int(input_val)
    except ValueError:
        return None


def level_4_real_world(raw_payload: dict[str, str]) -> dict[str, Any]:
    return {
        "id": int(raw_payload["id"]),
        "score": float(raw_payload["score"]),
        "active": raw_payload["active"].lower() in ("true", "1", "yes"),
    }


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium("")
    level_2_medium("Python")
    level_2_medium(0)
    level_2_medium([1, 2])

    print("\n--- Level 3 ---")
    print("Convert '123':", level_3_hard("123"))
    print("Convert 'abc':", level_3_hard("abc"))

    print("\n--- Level 4 ---")
    payload = {"id": "101", "score": "98.5", "active": "True"}
    parsed = level_4_real_world(payload)
    print("Parsed API Payload:", parsed)
    print("Types:", {k: type(v).__name__ for k, v in parsed.items()})
