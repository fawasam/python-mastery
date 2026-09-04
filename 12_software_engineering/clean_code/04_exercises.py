"""
Exercises: Refactoring Dirty Code into Clean Code.
"""


def refactor_nested_function(age: int, status: str, has_license: bool) -> str:
    """
    Refactor this dirty nested function using guard clauses:
    
    Original logic:
    if age >= 18:
        if status == "active":
            if has_license:
                return "APPROVED"
            else:
                return "NO_LICENSE"
        else:
            return "INACTIVE"
    else:
        return "UNDERAGE"
        
    Level 1 - Easy
    """
    raise NotImplementedError("Refactor using guard clauses")


def format_user_full_name(first_name: str | None, last_name: str | None, nickname: str | None) -> str:
    """
    Format user display name cleanly.
    If first & last present: "First Last (Nickname)" if nickname present, else "First Last"
    If only nickname: "Nickname"
    If all missing: "Anonymous"
    
    Level 2 - Medium
    """
    raise NotImplementedError("Implement clean display name formatter")
