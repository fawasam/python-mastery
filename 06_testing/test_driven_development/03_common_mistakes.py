"""
Common Mistakes in Test-Driven Development.
"""


# MISTAKE 1: Writing implementation code before writing tests
# Writing implementation first often leads to writing tests that conform to existing bugs rather than true specifications.
def mistake_code_first_without_test() -> None:
    pass


if __name__ == "__main__":
    print("Always write failing tests first (Red), implement code to pass (Green), then refactor!")
