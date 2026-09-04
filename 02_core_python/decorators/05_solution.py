"""
Topic: Decorator Solutions
File: 05_solution.py
"""
from functools import wraps
from typing import Any, Callable

def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"--> Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


def validate_positive(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argument {arg} must be positive")
        return func(*args, **kwargs)
    return wrapper


def memoize(func: Callable[..., Any]) -> Callable[..., Any]:
    cache: dict[tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in cache:
            print(f"  [Cache Miss] Computing {func.__name__}{args}")
            cache[args] = func(*args)
        else:
            print(f"  [Cache Hit] Returning cached {func.__name__}{args}")
        return cache[args]

    return wrapper


def require_role(role: str) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(user_context: dict[str, Any], *args: Any, **kwargs: Any) -> Any:
            user_roles = user_context.get("roles", [])
            if role not in user_roles:
                raise PermissionError(f"User lacks required role: '{role}'")
            return func(user_context, *args, **kwargs)
        return wrapper
    return decorator


if __name__ == "__main__":
    print("--- Level 1 ---")
    @log_calls
    def ping() -> None:
        print("pong")
    ping()

    print("\n--- Level 3 (Memoize) ---")
    @memoize
    def slow_square(n: int) -> int:
        return n * n
    slow_square(4)
    slow_square(4)

    print("\n--- Level 4 (RBAC) ---")
    @require_role("ADMIN")
    def delete_database(user: dict[str, Any]) -> None:
        print("Database deleted.")

    user_admin = {"name": "Alice", "roles": ["USER", "ADMIN"]}
    user_guest = {"name": "Bob", "roles": ["USER"]}

    delete_database(user_admin)
    try:
        delete_database(user_guest)
    except PermissionError as e:
        print("Caught expected permission error:", e)
