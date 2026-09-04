"""
Common Mistakes When Creating Custom Exceptions.
"""


# MISTAKE 1: Inheriting directly from BaseException
class BadSystemError(BaseException):
    """DANGER: standard 'except Exception:' blocks will NOT catch this!"""

    pass


# MISTAKE 2: Creating a custom exception without inheriting from Exception
class NotAnException:  # DANGER: Cannot raise objects that don't derive from BaseException!
    pass


# GOOD PRACTICE: Always inherit from Exception (or a library base exception)
class GoodAppError(Exception):
    pass


if __name__ == "__main__":
    print("--- Demonstrating Mistake 1 (BaseException) ---")
    try:
        try:
            raise BadSystemError("Critical System Failure")
        except Exception as e:
            print("This block NEVER runs because BadSystemError is not an Exception subclass!")
    except BadSystemError as e:
        print(f"Bypassed standard Exception catch and landed in BaseException handler: {e}")
