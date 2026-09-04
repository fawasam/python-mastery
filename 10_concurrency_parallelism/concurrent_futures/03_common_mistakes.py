"""
Common Mistakes in concurrent.futures.
"""


# MISTAKE 1: Forgetting to call future.result() or catch exceptions inside futures
def mistake_unhandled_future_exception() -> None:
    # DANGER: If a task submitted via executor.submit raises an exception,
    # the exception is stored on the Future object and IS NOT RAISED until future.result() is explicitly called!
    pass


if __name__ == "__main__":
    print("Always call future.result() or inspect future.exception() to handle exceptions thrown inside executor tasks!")
