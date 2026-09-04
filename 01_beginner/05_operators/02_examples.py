"""
Topic: Advanced Operator Examples (Identity vs Equality)
File: 02_examples.py
"""

def demonstrate_identity_vs_equality() -> None:
    # 1. Comparing primitive values vs lists
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = list_a

    print(f"list_a: {list_a} (id: {id(list_a)})")
    print(f"list_b: {list_b} (id: {id(list_b)})")
    print(f"list_c: {list_c} (id: {id(list_c)})")

    # Equality check (== compares values inside lists)
    print("\n--- Equality Check (==) ---")
    print(f"list_a == list_b: {list_a == list_b}")  # True because values match

    # Identity check (is compares memory addresses)
    print("\n--- Identity Check (is) ---")
    print(f"list_a is list_b: {list_a is list_b}")  # False because distinct objects in memory
    print(f"list_a is list_c: {list_a is list_c}")  # True because list_c points to list_a

    # Checking against None should ALWAYS use `is` or `is not`
    val = None
    print(f"\nIs val None? {val is None}")


if __name__ == "__main__":
    demonstrate_identity_vs_equality()
