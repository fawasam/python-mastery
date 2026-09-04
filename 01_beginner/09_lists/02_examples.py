"""
Topic: List Reference Semantics & Shallow/Deep Copying
File: 02_examples.py
"""
import copy

def demonstrate_copying_behavior() -> None:
    original = [1, 2, [3, 4]]

    # 1. Alias (same memory reference)
    alias = original
    alias[0] = 999
    print(f"Original after alias modification: {original}")  # Changed!

    # 2. Shallow Copy (.copy() or slice [:])
    shallow = original.copy()
    shallow[0] = 1  # Modifying primitive element in shallow copy does not affect original
    shallow[2][0] = 888  # BUT modifying nested mutable list DOES affect original!
    print(f"Original after shallow copy modification: {original}")

    # 3. Deep Copy (copy.deepcopy())
    deep = copy.deepcopy(original)
    deep[2][0] = 777  # Completely independent nested objects
    print(f"Original after deep copy modification:   {original}")
    print(f"Deep copy result:                         {deep}")


if __name__ == "__main__":
    demonstrate_copying_behavior()
