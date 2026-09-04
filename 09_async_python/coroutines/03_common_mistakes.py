"""
Common Mistakes in Coroutines.
"""


# MISTAKE 1: Re-using a closed coroutine
# Once a coroutine completes execution or is closed, attempting to await or send to it again
# raises RuntimeError: cannot reuse already awaited coroutine!
def mistake_reuse_coroutine() -> None:
    pass


if __name__ == "__main__":
    print("Coroutines can only be executed or awaited ONCE! Re-instantiate the function for subsequent calls.")
