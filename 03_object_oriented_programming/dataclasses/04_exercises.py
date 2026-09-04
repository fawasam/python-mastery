"""
Topic: Dataclass Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a `@dataclass` `UserDTO` with fields `id: int`, `email: str`, and default `is_active: bool = True`.
    """
    # TODO: Create UserDTO dataclass
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create a `@dataclass` `Order` with `items: list[str] = field(default_factory=list)`. Add `__post_init__` validating order has >= 1 item.
    """
    # TODO: Create Order dataclass
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Create a frozen dataclass `ConfigKey(section: str, key: str)` and use it as a dictionary key in a settings registry.
    """
    # TODO: Frozen dataclass as dict key
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an API response schema dataclass `APIResponseData` with helper method `to_json_dict()` returning a clean JSON-serializable dictionary.
    """
    # TODO: API Response dataclass
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
