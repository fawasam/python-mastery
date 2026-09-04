"""
Topic: Composition Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a `CPU` class and a `RAM` class. Create a `Computer` class composed of CPU and RAM objects.
    """
    # TODO: Implement Computer composition
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create an `Author` class and a `Book` class where `Book` HAS-AN `Author`.
    """
    # TODO: Implement Book-Author composition
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Create an `Order` composed of a list of `OrderItem` objects. Add `calculate_total()` method iterating over items.
    """
    # TODO: Implement Order-OrderItem composition
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an e-commerce `OrderProcessor` composed of a `PaymentGateway`, `InventoryService`, and `EmailNotifier`.
    """
    # TODO: Implement OrderProcessor composition architecture
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
