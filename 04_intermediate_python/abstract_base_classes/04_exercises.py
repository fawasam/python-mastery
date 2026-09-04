"""
Topic: ABC Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create an ABC `Serializer(ABC)` with `@abstractmethod` `serialize(data: dict) -> str`. Derive `JSONSerializer`.
    """
    # TODO: Implement Serializer ABC
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create an ABC `BaseRepository(ABC)` declaring `find_by_id(id)` and `save(entity)`. Implement `InMemoryRepository`.
    """
    # TODO: Implement BaseRepository ABC
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Register an existing third-party class as a virtual subclass of an ABC using `ABC.register()`.
    """
    # TODO: Virtual subclass registration
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build a microservice health check contract `BaseHealthCheck(ABC)` with abstract property `service_name` and abstract method `check_health() -> bool`.
    """
    # TODO: BaseHealthCheck contract
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
