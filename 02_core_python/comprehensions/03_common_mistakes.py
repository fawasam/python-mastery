"""
Topic: Common Mistakes with Comprehensions
File: 03_common_mistakes.py
"""

def mistake_1_overly_complex_comprehension() -> None:
    # ❌ WRONG: Deeply nested, unreadable comprehension
    # result = [f(x, y) for x in range(10) if x > 2 for y in range(x) if y % 2 == 0 and x + y < 15]

    # ✅ CORRECT: If logic spans multiple nested clauses or conditionals, use a standard for loop for clarity!
    print("If a comprehension exceeds 2 lines or has >2 loops, refactor to explicit for loops.")


def mistake_2_if_else_positioning() -> None:
    # Filtering IF goes AFTER the for loop: [x for x in data if x > 0]
    # Conditional IF-ELSE value expression goes BEFORE the for loop: [x if x > 0 else 0 for x in data]

    data = [-2, 5, -1, 3]
    clamped = [x if x > 0 else 0 for x in data]
    print(f"Clamped non-negative numbers: {clamped}")


if __name__ == "__main__":
    mistake_1_overly_complex_comprehension()
    mistake_2_if_else_positioning()
