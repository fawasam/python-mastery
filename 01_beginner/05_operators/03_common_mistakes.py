"""
Topic: Common Mistakes with Operators
File: 03_common_mistakes.py
"""

def mistake_1_using_is_for_value_equality() -> None:
    # ❌ WRONG: comparing strings or integers using `is`
    # a = 1000
    # b = 1000
    # if a is b: ... (May return False for large numbers because they aren't interned)
    
    # ✅ CORRECT: Use == for value comparisons, reserve `is` for `None` or singleton checks.
    a = 1000
    b = 1000
    print(f"a == b is {a == b}")


def mistake_2_chained_comparison_misunderstandings() -> None:
    # Python supports elegant chained comparisons: 10 < x < 20
    # In C++ or Java, 10 < x < 20 means (10 < x) < 20, which is a bug!
    # Python converts 10 < x < 20 to (10 < x) and (x < 20).
    
    x = 15
    print(f"Is 10 < x < 20? {10 < x < 20}")


def mistake_3_operator_precedence() -> None:
    # Multiplication (*) has higher precedence than Addition (+)
    # 2 + 3 * 4 = 14, not 20!
    # Use parentheses explicitly to clarify intent.
    result = (2 + 3) * 4
    print(f"(2 + 3) * 4 = {result}")


if __name__ == "__main__":
    mistake_1_using_is_for_value_equality()
    mistake_2_chained_comparison_misunderstandings()
    mistake_3_operator_precedence()
