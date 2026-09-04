"""
Topic: Polymorphism Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create classes `Dog` and `Cat` with a `speak()` method. Write a function `animal_sound(animal)` calling `animal.speak()`.
    """
    # TODO: Implement duck-typed speak
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create custom logger classes `FileLogger` and `ConsoleLogger` with `.log(msg)`. Write a polymorphic batch logger function.
    """
    # TODO: Implement batch logger
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Implement polymorphic document converters `MarkdownToHtml` and `TextToHtml` with `.convert(source: str) -> str`.
    """
    # TODO: Implement document converters
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build a polymorphic cloud storage abstraction (`S3Storage`, `GCSStorage`, `LocalStorage`) with `.upload(filename, data)`.
    """
    # TODO: Implement Cloud Storage adapters
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
