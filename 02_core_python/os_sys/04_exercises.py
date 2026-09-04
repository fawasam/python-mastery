"""
Topic: OS and Sys Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Read environment variable `"PORT"`. If missing, return default integer `8080`.
    """
    # TODO: Read PORT env var
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Parse positional CLI arguments from `sys.argv[1:]` and print each with its index.
    """
    # TODO: Print sys.argv arguments
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Write a function `get_system_info()` returning a dict with keys `os_name`, `platform`, `python_version`, and `process_id`.
    """
    # TODO: Get system info dict
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an environment validation bootstrap script `bootstrap_env(required_keys: list[str])`.
    If any key is missing from `os.environ`, print errors to `sys.stderr` and exit with code 1.
    """
    # TODO: Implement environment validator
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
