"""
Topic: Context Manager Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a `@contextmanager` function `temporary_setting(settings: dict, key: str, temp_value: str)` that temporarily overrides a dictionary setting inside the block and restores original value on exit.
    """
    # TODO: Implement temporary setting context manager
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create a custom class context manager `DatabaseTransactionManager()` that prints `"BEGIN TRANSACTION"` on enter, and `"COMMIT TRANSACTION"` on exit (or `"ROLLBACK TRANSACTION"` if exception occurs).
    """
    # TODO: Implement database transaction context manager
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Implement a `@contextmanager` function `redirect_stdout_to_string()` that captures all standard output prints inside the block into a StringIO buffer and yields the buffer.
    """
    # TODO: Implement stdout redirect context manager
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an atomic file writer context manager `atomic_write(file_path: Path)` that writes data to a temporary file `.tmp` and renames it atomically to target path only if no exceptions occur.
    """
    # TODO: Implement atomic file writer context manager
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
