"""
Common Mistakes in Flask Web Applications.
"""


# MISTAKE 1: Accessing global Flask context variables outside of a request context
def mistake_outside_request_context() -> None:
    # DANGER: Accessing 'from flask import request; print(request.args)' outside a route handler or test_request_context()
    # raises RuntimeError: Working outside of request context!
    pass


if __name__ == "__main__":
    print("Flask request objects ('request', 'g') exist ONLY during active HTTP request contexts!")
