"""
Topic: Protocol Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Define a `Drawable` Protocol with method `draw() -> None`.
    """
    # TODO: Define Drawable protocol
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create a `@runtime_checkable` protocol `Closeable` with method `close() -> None`.
    """
    # TODO: Define Closeable protocol
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Define a `SerializerProtocol[T]` protocol for objects capable of serializing domain entities of type `T`.
    """
    # TODO: Generic SerializerProtocol
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an HTTP Client protocol `HTTPClientProtocol` requiring `get(url: str) -> dict` and `post(url: str, json_data: dict) -> dict`.
    """
    # TODO: HTTPClientProtocol
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
