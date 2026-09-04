"""
Topic: Flexibly Accepting Arguments with *args and **kwargs
File: 02_examples.py
"""
from typing import Any

def log_event(event_name: str, *tags: str, **context: Any) -> None:
    """
    Structured logger receiving variable tags and arbitrary key-value metadata.
    """
    tag_str = ", ".join(f"[{t}]" for t in tags) if tags else "[NO_TAGS]"
    print(f"EVENT: {event_name} | TAGS: {tag_str}")
    
    if context:
        print("  METADATA:")
        for key, val in context.items():
            print(f"    - {key}: {val}")


if __name__ == "__main__":
    log_event(
        "USER_LOGIN_SUCCESS",
        "SECURITY",
        "AUTH",
        user_id=8841,
        ip_address="192.168.1.50",
        attempt_count=1,
    )
