"""
Fixture Exercises.
"""

from typing import Generator


class TemporaryFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.is_open = True

    def write(self, content: str) -> None:
        pass

    def delete(self) -> None:
        self.is_open = False


# Exercise 1 (Medium): Write a yield fixture function temp_file_fixture()
# Setup: instantiate TemporaryFile("test.tmp")
# Yield: the temp_file instance
# Teardown: call temp_file.delete()
def temp_file_fixture() -> Generator[TemporaryFile, None, None]:
    raise NotImplementedError("Implement temp_file_fixture")
