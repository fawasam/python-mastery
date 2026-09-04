"""
Common Mistakes in Integration Testing.
"""


# MISTAKE 1: Over-mocking in Integration Tests
# If you mock the database connection in an integration test, you are no longer testing database integration!
def mistake_overmocking_integration() -> None:
    # DANGER: Mocking DB driver in integration test bypasses real SQL syntax verification!
    pass


if __name__ == "__main__":
    print("Integration tests must use actual external services or accurate local emulators (e.g. SQLite :memory:).")
