"""
Topic: Exception Solutions
File: 05_solution.py
"""
from typing import Any

def level_1_easy(val: str) -> int:
    try:
        res = int(val)
        print(f"Casted '{val}' -> {res}")
        return res
    except ValueError:
        print(f"Failed casting '{val}', returning 0")
        return 0


def level_2_medium(d: dict[str, Any], key: str, default: Any = None) -> Any:
    try:
        val = d[key]
        print(f"Found key '{key}': {val}")
        return val
    except KeyError:
        print(f"Key '{key}' missing. Returning default: {default}")
        return default


def level_3_hard(items: Any, index: int) -> Any:
    try:
        val = items[index]
        print(f"items[{index}] = {val}")
        return val
    except IndexError:
        print(f"IndexError: Index {index} out of bounds for sequence of length {len(items)}")
        return None
    except TypeError as e:
        print(f"TypeError: Object is not subscriptable ({e})")
        return None


def level_4_real_world(payload: dict[str, Any]) -> str:
    if "user" not in payload:
        raise ValueError("Missing 'user' object in payload")
    user = payload["user"]
    if not isinstance(user, dict) or "id" not in user:
        raise ValueError("User object must contain an 'id' field")
    
    user_id = str(user["id"])
    print(f"Extracted User ID: {user_id}")
    return user_id


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy("42")
    level_1_easy("bad")

    print("\n--- Level 2 ---")
    level_2_medium({"a": 1}, "b", default=100)

    print("\n--- Level 3 ---")
    level_3_hard([10, 20], 5)
    level_3_hard(12345, 0)

    print("\n--- Level 4 ---")
    try:
        level_4_real_world({"user": {"id": "usr_7721"}})
        level_4_real_world({"invalid": True})
    except ValueError as err:
        print("Caught validation error:", err)
