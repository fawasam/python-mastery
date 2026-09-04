"""
Topic: Encapsulation Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a `BankAccount` class with private attribute `__balance`. Provide getter `get_balance()` and deposit method.
    """
    # TODO: Implement BankAccount encapsulation
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create a `Temperature` class with protected `_celsius` attribute and validation setter enforcing `celsius >= -273.15`.
    """
    # TODO: Implement Temperature validation
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Demonstrate name mangling by inheriting from a class with private attribute `__id` and accessing both parent and child mangled attributes.
    """
    # TODO: Name mangling inheritance demo
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an encapsulated API Token Session class `APISession` managing private `__token` refresh state.
    """
    # TODO: Encapsulated APISession
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
