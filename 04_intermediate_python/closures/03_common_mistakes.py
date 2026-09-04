"""
Common Mistakes with Python Closures.
"""

from typing import Callable


# MISTAKE 1: Late binding of variables inside loop-generated closures
def create_multipliers_buggy() -> list[Callable[[int], int]]:
    funcs = []
    # 'i' is captured by reference, NOT by value at loop iteration time!
    for i in range(4):
        funcs.append(lambda x: x * i)
    return funcs


# FIX 1: Use default argument values to bind current iteration value eagerly
def create_multipliers_fixed() -> list[Callable[[int], int]]:
    funcs = []
    for i in range(4):
        funcs.append(lambda x, i=i: x * i)
    return funcs


# MISTAKE 2: Reassigning an outer scope variable without 'nonlocal'
def make_counter_buggy():
    count = 0

    def increment():
        # DANGER: UnboundLocalError! Python sees 'count =' and treats count as local,
        # but attempts to read count on the RHS before assignment!
        # count = count + 1  <-- Uncommenting this causes runtime failure
        pass

    return increment


if __name__ == "__main__":
    print("--- Mistake 1: Late Binding in Loops ---")
    buggy_funcs = create_multipliers_buggy()
    results_buggy = [f(10) for f in buggy_funcs]
    print(f"Buggy (expected [0, 10, 20, 30]): Got {results_buggy}")

    print("\n--- Fix 1: Early Binding via Default Arguments ---")
    fixed_funcs = create_multipliers_fixed()
    results_fixed = [f(10) for f in fixed_funcs]
    print(f"Fixed: Got {results_fixed}")
