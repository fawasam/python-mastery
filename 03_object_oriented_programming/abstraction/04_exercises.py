"""
Topic: Abstraction Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Define an ABC `Animal(ABC)` with `@abstractmethod` `sound()`. Derive `Dog` and `Cat` classes implementing `sound()`.
    """
    # TODO: Implement Animal ABC
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Define an ABC `CacheStorage(ABC)` with abstract methods `get(key)` and `set(key, val)`. Implement concrete `InMemoryCache`.
    """
    # TODO: Implement CacheStorage ABC
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Define an ABC `DocumentParser(ABC)` with `@abstractmethod` `parse(raw_content: str) -> dict`. Implement `JSONParser` and `KeyValueParser`.
    """
    # TODO: Implement DocumentParser ABC
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an ETL Data Pipeline ABC `BaseDataPipeline(ABC)` declaring `@abstractmethod` `extract()`, `transform()`, `load()`, and a concrete `run()` pipeline orchestrator method.
    """
    # TODO: Implement BaseDataPipeline Template Method pattern
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
