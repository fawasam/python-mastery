"""
Basic Guard Clauses and Defensive Copying in Python.
"""


class User:
    def __init__(self, username: str, is_active: bool) -> None:
        self.username = username
        self.is_active = is_active


def process_user_checkout(user: User | None, cart: list[str]) -> str:
    # 1. Guard Clause: Fail fast if user is missing or inactive
    if user is None:
        raise ValueError("User must not be None")
    if not user.is_active:
        raise PermissionError(f"User '{user.username}' is not active")

    # 2. Guard Clause: Fail fast if cart is empty
    if not cart:
        raise ValueError("Cart contains no items to checkout")

    # Primary business logic runs clean without nested indentation!
    item_count = len(cart)
    return f"Successfully processed checkout of {item_count} item(s) for {user.username}"


class ConfigurationManager:
    def __init__(self, settings: dict[str, str]) -> None:
        # Defensive copy on input: prevent caller from mutating dictionary afterwards
        self._settings = settings.copy()

    def get_settings(self) -> dict[str, str]:
        # Defensive copy on output: prevent caller from mutating internal state
        return self._settings.copy()


if __name__ == "__main__":
    user = User("alice", is_active=True)
    cart = ["Book", "Laptop Stand"]

    summary = process_user_checkout(user, cart)
    print(summary)
