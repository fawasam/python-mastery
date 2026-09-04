"""
Topic: Common Mistakes with Unpacking
File: 03_common_mistakes.py
"""

def mistake_1_mismatched_element_count() -> None:
    # ❌ WRONG: a, b = [1, 2, 3] -> ValueError: too many values to unpack (expected 2)
    # ❌ WRONG: a, b, c = [1] -> ValueError: not enough values to unpack (expected 3, got 1)

    # ✅ CORRECT: Match exact element count OR use starred `*rest` to capture remaining elements
    a, *rest = [1, 2, 3]
    print(f"a = {a}, rest = {rest}")


def mistake_2_multiple_starred_expressions() -> None:
    # ❌ WRONG: *head, *tail = [1, 2, 3, 4] -> SyntaxError: two starred expressions in assignment

    # ✅ CORRECT: At most ONE starred expression is allowed per assignment target!
    head, *middle, tail = [1, 2, 3, 4]
    print(f"head={head}, middle={middle}, tail={tail}")


if __name__ == "__main__":
    mistake_1_mismatched_element_count()
    mistake_2_multiple_starred_expressions()
