"""
Topic: Common Mistakes with Functions
File: 03_common_mistakes.py
"""

# ❌ WRONG: Mutable default argument!
def append_to_list_buggy(element: int, target_list: list[int] = []) -> list[int]:
    # Default parameter [] is evaluated ONCE when function is defined, NOT on each call!
    # All callers sharing the default list will mutate the exact same object!
    target_list.append(element)
    return target_list


# ✅ CORRECT: Use None as default value and initialize inside function
def append_to_list_correct(element: int, target_list: list[int] | None = None) -> list[int]:
    if target_list is None:
        target_list = []
    target_list.append(element)
    return target_list


if __name__ == "__main__":
    print("--- Demonstrating Buggy Mutable Default ---")
    res1 = append_to_list_buggy(1)
    res2 = append_to_list_buggy(2)
    print(f"Buggy call 2 result: {res2}")  # Prints [1, 2] instead of [2]!

    print("\n--- Demonstrating Correct Pattern ---")
    res3 = append_to_list_correct(1)
    res4 = append_to_list_correct(2)
    print(f"Correct call 2 result: {res4}")  # Prints [2] independently!
