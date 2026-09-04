"""
Topic: Set Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Convert list `[10, 20, 10, 30, 20, 40]` to a set and check if `30` exists in it.
    """
    # TODO: Deduplicate list and check membership
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Given sets `required_permissions = {"read", "write", "execute"}` and `granted_permissions = {"read", "write"}`,
    find the missing permissions needed.
    """
    # TODO: Find set difference
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Given two lists of customer emails from System A and System B,
    return a tuple containing: (common_emails, unique_to_A, unique_to_B).
    """
    # TODO: Set operations on customer lists
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Implement a fast bad-word content filter function `censor_text(text: str, banned_words: set[str]) -> str`.
    Replace any banned word in text with `"***"`.
    """
    # TODO: Implement fast set-based text censoring
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
