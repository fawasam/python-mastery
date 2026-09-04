"""
Topic: Pathlib Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a Path object for `temp/cache/data.bin`. Print its stem and suffix.
    """
    # TODO: Print stem and suffix
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Safely create nested directory `build/artifacts/logs` using `.mkdir(parents=True, exist_ok=True)`.
    """
    # TODO: Create nested directory
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Calculate total size in bytes of all `.py` files in the current folder.
    """
    # TODO: Calculate total size
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an automated directory organizer function `organize_directory(target_dir: Path)` that moves `.txt` files into `target_dir/texts/` and `.png` into `target_dir/images/`.
    """
    # TODO: Implement directory file organizer
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
