"""
Solutions for Authorization Exercises.
"""


def check_scope_permission(user_scopes: list[str], required_scope: str) -> bool:
    return "admin:all" in user_scopes or required_scope in user_scopes


if __name__ == "__main__":
    assert check_scope_permission(["read:users", "write:users"], "write:users") is True
    assert check_scope_permission(["read:users"], "write:users") is False
    assert check_scope_permission(["admin:all"], "write:users") is True
    print("Scope permission checker exercise passed successfully!")
