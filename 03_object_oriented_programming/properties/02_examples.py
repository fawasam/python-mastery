"""
Topic: Read-Only Property Pattern
File: 02_examples.py
"""

class UserSession:
    def __init__(self, user_id: int) -> None:
        self._user_id = user_id

    # Read-only property (no setter defined!)
    @property
    def user_id(self) -> int:
        return self._user_id


if __name__ == "__main__":
    session = UserSession(9901)
    print(f"User ID: {session.user_id}")

    try:
        session.user_id = 1000  # AttributeError: property 'user_id' of 'UserSession' object has no setter
    except AttributeError as err:
        print(f"Caught expected AttributeError when attempting to overwrite read-only property: {err}")
