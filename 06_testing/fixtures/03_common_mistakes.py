"""
Common Mistakes in Pytest Fixtures.
"""


# MISTAKE: Sharing mutable state across test functions via module scope without cleanup
class SharedDatabaseState:
    shared_list: list[str] = []


def mistake_shared_state_pollution() -> None:
    db = SharedDatabaseState()
    db.shared_list.append("Dirty State From Test A")


if __name__ == "__main__":
    mistake_shared_state_pollution()
    print(f"Polluted Shared State: {SharedDatabaseState.shared_list}")
