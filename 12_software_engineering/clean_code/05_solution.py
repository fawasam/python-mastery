"""
Solutions: Clean Code Refactoring Exercises.
"""


def refactor_nested_function(age: int, status: str, has_license: bool) -> str:
    """
    Refactored using guard clauses to eliminate nested conditionals.
    """
    if age < 18:
        return "UNDERAGE"
        
    if status != "active":
        return "INACTIVE"
        
    if not has_license:
        return "NO_LICENSE"
        
    return "APPROVED"


def format_user_full_name(first_name: str | None, last_name: str | None, nickname: str | None) -> str:
    """
    Cleanly formatted user name using concise python string building.
    """
    if first_name and last_name:
        base = f"{first_name} {last_name}"
        return f"{base} ({nickname})" if nickname else base
        
    if nickname:
        return nickname
        
    return "Anonymous"


if __name__ == "__main__":
    print("Approval check:", refactor_nested_function(20, "active", True))
    print("Formatted name:", format_user_full_name("John", "Doe", "Johnny"))
