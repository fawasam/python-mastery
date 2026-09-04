"""
Topic: Common Mistakes with Tuples
File: 03_common_mistakes.py
"""

def mistake_1_forgetting_trailing_comma_single_tuple() -> None:
    # ❌ WRONG: single_item = ("hello") -> Returns string "hello", NOT a tuple!
    not_a_tuple = ("hello")
    print(f"not_a_tuple type: {type(not_a_tuple).__name__}")

    # ✅ CORRECT: Single-element tuples REQUIRE a trailing comma!
    real_tuple = ("hello",)
    print(f"real_tuple type:  {type(real_tuple).__name__}")


def mistake_2_attempting_item_assignment() -> None:
    coords = (10, 20)

    # ❌ WRONG: coords[0] = 15 -> TypeError: 'tuple' object does not support item assignment
    # ✅ CORRECT: Construct a new tuple if values need to change
    new_coords = (15, coords[1])
    print(f"New tuple: {new_coords}")


if __name__ == "__main__":
    mistake_1_forgetting_trailing_comma_single_tuple()
    mistake_2_attempting_item_assignment()
