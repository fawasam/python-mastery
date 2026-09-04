"""
Topic: Common Mistakes with Sets
File: 03_common_mistakes.py
"""

def mistake_1_empty_set_initialization() -> None:
    # ❌ WRONG: empty_val = {}
    # `{}` creates an empty DICTIONARY, not a set!
    empty_dict = {}
    print(f"Type of {{}}: {type(empty_dict).__name__}")

    # ✅ CORRECT: Use set() for an empty set
    real_empty_set = set()
    print(f"Type of set(): {type(real_empty_set).__name__}")


def mistake_2_unhashable_set_elements() -> None:
    # ❌ WRONG: invalid_set = {[1, 2], [3, 4]}
    # Lists are mutable (unhashable) and CANNOT be added to a set!
    # TypeError: unhashable type: 'list'

    # ✅ CORRECT: Use tuples for immutable elements inside a set!
    valid_set = {(1, 2), (3, 4)}
    print(f"Set of tuples: {valid_set}")


if __name__ == "__main__":
    mistake_1_empty_set_initialization()
    mistake_2_unhashable_set_elements()
