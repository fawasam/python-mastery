"""
Topic: Common Mistakes with Map and Filter
File: 03_common_mistakes.py
"""

def mistake_1_exhausting_map_iterator() -> None:
    # ❌ TRAP: map() returns a single-pass iterator!
    result_map = map(lambda x: x * 2, [1, 2, 3])

    # First pass consumes all elements:
    first_pass = list(result_map)
    print(f"First pass:  {first_pass}")

    # Second pass will be EMPTY because iterator was exhausted!
    second_pass = list(result_map)
    print(f"Second pass: {second_pass}")  # Prints []!

    # ✅ CORRECT: Convert to list immediately if reusing results multiple times!


if __name__ == "__main__":
    mistake_1_exhausting_map_iterator()
