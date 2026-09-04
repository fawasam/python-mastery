"""
Common Mistakes in Web Middleware Design.
"""


# MISTAKE 1: Forgetting to return response from call_next in FastAPI middleware
def mistake_forgot_call_next_return() -> None:
    # DANGER: If middleware executes await call_next(request) but fails to return response,
    # caller receives 500 error or empty connection timeout!
    pass


if __name__ == "__main__":
    print("Always return response object returned by call_next(request) in HTTP middleware handlers!")
