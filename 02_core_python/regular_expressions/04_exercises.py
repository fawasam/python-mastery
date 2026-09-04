"""
Topic: Regex Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Write a regex pattern to extract all phone numbers matching `XXX-XXX-XXXX` from text.
    """
    # TODO: Phone number extraction
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Validate password strength using regex: must contain >= 8 chars, 1 uppercase, 1 lowercase, 1 digit.
    """
    # TODO: Validate password regex
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Convert markdown bold text `**hello**` to HTML `<b>hello</b>` using `re.sub()`.
    """
    # TODO: Markdown bold to HTML sub
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Extract and parse key-value query parameters from a URL string using regex named groups.
    """
    # TODO: URL parameter parser
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
