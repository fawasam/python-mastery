"""
Topic: Datetime Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Calculate the exact number of days between `"2026-01-01"` and `"2026-12-31"`.
    """
    # TODO: Calculate days difference
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Parse date string `"04/Sep/2026 14:30"` into a datetime object using `strptime()`.
    """
    # TODO: Parse date string
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Write a function `is_token_expired(created_at: datetime, ttl_seconds: int = 3600) -> bool`.
    """
    # TODO: Check token expiry
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build a business day calculator `add_business_days(start_date: date, num_days: int) -> date` skipping weekends (Saturday & Sunday).
    """
    # TODO: Implement business day calculator
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
