"""
Topic: Inheritance Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a base class `Vehicle(brand, speed)` with method `drive()`. Create a subclass `ElectricCar(brand, speed, battery_capacity)` overriding `drive()`.
    """
    # TODO: Create Vehicle and ElectricCar classes
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create a base class `Shape` with `area()` method. Derive `Rectangle(w, h)` and `Circle(r)`.
    """
    # TODO: Create Shape hierarchy
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Implement multiple inheritance with mixin classes `JSONMixin` and `LoggerMixin` on an `Order` domain model.
    """
    # TODO: Implement Mixin classes
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an authentication hierarchy: base `BaseAuth` with method `authenticate()`, subclass `JWTAuth(secret)` and subclass `APIKeyAuth(key)`.
    """
    # TODO: Implement Auth hierarchy
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
