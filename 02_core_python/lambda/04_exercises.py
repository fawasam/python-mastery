"""
Topic: Lambda Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Sort a list of strings `["apple", "fig", "banana", "kiwi"]` by word length using `sorted()` and a lambda.
    """
    # TODO: Sort by length
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Given a list of coordinate tuples `[(1, 5), (3, 2), (2, 8)]`, sort them by the second element ascending using lambda.
    """
    # TODO: Sort by second item
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Sort a list of product dictionaries by stock status (in-stock first), then by price ascending using a compound tuple lambda key.
    """
    # TODO: Multi-key sorting
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an event listener registry `register_handler(event_name, handler_func)` where handlers can be passed as inline lambdas.
    """
    # TODO: Implement event handler registry
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
