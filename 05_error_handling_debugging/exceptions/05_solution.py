"""
Solutions for Exception Handling Exercises.
"""


def parse_int_with_default(raw_value: str, default: int) -> int:
    try:
        return int(raw_value)
    except (ValueError, TypeError):
        return default


if __name__ == "__main__":
    print(f"Parsed '123': {parse_int_with_default('123', 0)}")
    print(f"Parsed 'invalid': {parse_int_with_default('invalid', 0)}")
