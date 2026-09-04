"""
Topic: Classes Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a `Book` class with attributes `title`, `author`, `pages`. Add a method `summary()` returning `"Title by Author (X pages)"`.
    """
    # TODO: Create Book class
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create a `BankAccount` class with `balance` and methods `deposit(amt)` and `withdraw(amt)`. Prevent withdrawals if `amt > balance`.
    """
    # TODO: Create BankAccount class
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Create a `Student` class with a list attribute `grades`. Add `add_grade(grade)` and `get_average()` methods.
    """
    # TODO: Create Student class
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an `InventoryItem` domain model class with `sku`, `price`, `quantity`, and methods `restock(qty)` and `calculate_total_value()`.
    """
    # TODO: Implement InventoryItem class
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
