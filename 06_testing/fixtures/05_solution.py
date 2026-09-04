"""
Solutions for Fixture Exercises.
"""

from typing import Generator


class TemporaryFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.is_open = True

    def delete(self) -> None:
        self.is_open = False


def temp_file_fixture() -> Generator[TemporaryFile, None, None]:
    tf = TemporaryFile("test.tmp")
    try:
        yield tf
    finally:
        tf.delete()


if __name__ == "__main__":
    gen = temp_file_fixture()
    file_obj = next(gen)
    assert file_obj.is_open is True
    print("Fixture yielded open temporary file.")

    try:
        next(gen)
    except StopIteration:
        pass
    assert file_obj.is_open is False
    print("Fixture teardown executed successfully!")
