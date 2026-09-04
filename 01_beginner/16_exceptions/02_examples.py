"""
Topic: User Input Sanitization with Exception Handling
File: 02_examples.py
"""

def parse_user_age(raw_input: str) -> int:
    try:
        age = int(raw_input)
        if age < 0 or age > 120:
            raise ValueError(f"Age {age} is outside valid human range (0..120).")
    except ValueError as e:
        print(f"Validation Error: {e}")
        raise e
    else:
        print(f"Valid age parsed: {age}")
        return age


if __name__ == "__main__":
    try:
        parse_user_age("25")
        parse_user_age("invalid_number")
    except ValueError:
        print("Caught expected validation exception gracefully.")
