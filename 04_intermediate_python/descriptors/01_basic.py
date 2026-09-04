"""
Basic Descriptor Protocol in Python.

This module introduces the fundamental descriptor methods: __get__, __set__, and __set_name__.
"""


class VerboseAttribute:
    """
    A simple descriptor that prints access and modification logs.
    """

    def __set_name__(self, owner: type, name: str) -> None:
        # __set_name__ runs automatically when the class is constructed.
        # It captures the attribute name assigned in the owner class.
        self.public_name = name
        self.private_name = f"_{name}"

    def __get__(self, instance: object | None, owner: type | None = None) -> object:
        # Accessing from class level (e.g., User.name) passes instance=None
        if instance is None:
            return self

        value = getattr(instance, self.private_name, None)
        print(f"[LOG] Getting '{self.public_name}': {value}")
        return value

    def __set__(self, instance: object, value: object) -> None:
        print(f"[LOG] Setting '{self.public_name}' to {value}")
        setattr(instance, self.private_name, value)


class User:
    # Descriptors MUST be declared as class attributes, not instance attributes
    username = VerboseAttribute()
    email = VerboseAttribute()

    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email


if __name__ == "__main__":
    user = User("alice", "alice@example.com")
    print(f"Username is: {user.username}")
    user.username = "alice_v2"
    print(f"Updated username is: {user.username}")
