"""
Basic Pytest Fixture Simulation.
"""

from typing import Generator


class DatabaseSession:
    def __init__(self) -> None:
        self.is_connected = True
        self.data: list[str] = ["initial_record"]

    def close(self) -> None:
        self.is_connected = False


# Generator-based yield fixture simulation pattern
def db_session_fixture() -> Generator[DatabaseSession, None, None]:
    # Setup Phase
    print("\n[FIXTURE SETUP] Opening test database session...")
    db = DatabaseSession()
    try:
        yield db
    finally:
        # Teardown Phase
        print("[FIXTURE TEARDOWN] Closing database session...")
        db.close()


def test_db_read_record() -> None:
    fixture_gen = db_session_fixture()
    db = next(fixture_gen)  # Trigger fixture setup

    assert db.is_connected is True
    assert "initial_record" in db.data

    try:
        next(fixture_gen)  # Trigger fixture teardown
    except StopIteration:
        pass


if __name__ == "__main__":
    test_db_read_record()
