"""
Common Mistakes in Defensive Programming.
"""


# MISTAKE 1: Over-defensive programming (paranoia)
# Validating internal parameters in private methods where invariants are already guaranteed
def bad_over_defensive(x: int) -> int:
    # Overkill if x is internal and already type-checked by static analyzer / caller
    if not isinstance(x, int):
        raise TypeError(...)
    if x is None:
        raise ValueError(...)
    return x * 2


# MISTAKE 2: Returning mutable internal references directly
class BadRepository:
    def __init__(self) -> None:
        self._records: list[str] = ["record1", "record2"]

    def get_records(self) -> list[str]:
        # DANGER: Caller can call repo.get_records().clear() and wipe out repo internal state!
        return self._records


class GoodRepository:
    def __init__(self) -> None:
        self._records: list[str] = ["record1", "record2"]

    def get_records(self) -> list[str]:
        # GOOD: Returns defensive copy
        return self._records.copy()


if __name__ == "__main__":
    bad_repo = BadRepository()
    records = bad_repo.get_records()
    records.clear()
    print(f"Bad Repo internal state mutated by caller: {bad_repo.get_records()}")

    good_repo = GoodRepository()
    records = good_repo.get_records()
    records.clear()
    print(f"Good Repo internal state preserved safely: {good_repo.get_records()}")
