"""
Topic: Common Mistakes with Decorators
File: 03_common_mistakes.py
"""
from functools import wraps

def mistake_1_forgetting_functools_wraps() -> None:
    def buggy_decorator(func):
        # ❌ WRONG: Missing @wraps(func)!
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    @buggy_decorator
    def get_user_id() -> int:
        """Returns the logged in user ID."""
        return 404

    # Function metadata is LOST! __name__ becomes "wrapper" instead of "get_user_id"!
    print(f"Lost name metadata: {get_user_id.__name__}")  # Prints 'wrapper'


if __name__ == "__main__":
    mistake_1_forgetting_functools_wraps()
