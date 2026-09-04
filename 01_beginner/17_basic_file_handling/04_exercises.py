"""
Topic: File Handling Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a file named `notes.txt`, write `"Python Mastery Course"` to it, and read it back.
    """
    # TODO: Write and read text file
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Write a function `count_lines_in_file(path: Path) -> int` that counts non-empty lines in a given text file.
    """
    # TODO: Count non-empty lines
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Read a log file and extract all lines containing `"ERROR"`. Save extracted log lines to `errors.log`.
    """
    # TODO: Extract and write error logs
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an atomic JSON log writer function `append_json_log(log_path: Path, entry: dict)` using `pathlib` and UTF-8 encoding.
    """
    # TODO: Implement atomic JSON logger
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
