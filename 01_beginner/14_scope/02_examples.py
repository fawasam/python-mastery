"""
Topic: Modifying Scope with global and nonlocal
File: 02_examples.py
"""

GLOBAL_COUNTER = 0

def update_global_counter() -> None:
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 1
    print(f"Global counter updated to: {GLOBAL_COUNTER}")


def make_counter_closure():
    count = 0  # Enclosing variable

    def counter() -> int:
        nonlocal count  # Binds to outer 'count' variable
        count += 1
        return count

    return counter


if __name__ == "__main__":
    print("--- Global Scope Modification ---")
    update_global_counter()
    update_global_counter()

    print("\n--- Nonlocal Closure Counter ---")
    my_counter = make_counter_closure()
    print("Call 1:", my_counter())
    print("Call 2:", my_counter())
    print("Call 3:", my_counter())
