"""
Topic: Protocol Solutions
File: 05_solution.py
"""
from typing import Any, Protocol, runtime_checkable

class Drawable(Protocol):
    def draw(self) -> None:
        ...


@runtime_checkable
class Closeable(Protocol):
    def close(self) -> None:
        ...


class FileHandler:
    def close(self) -> None:
        print("FileHandler closed.")


class HTTPClientProtocol(Protocol):
    def get(self, url: str) -> dict[str, Any]:
        ...

    def post(self, url: str, json_data: dict[str, Any]) -> dict[str, Any]:
        ...


class MockHTTPClient:
    def get(self, url: str) -> dict[str, Any]:
        print(f"[Mock GET] {url}")
        return {"status": 200}

    def post(self, url: str, json_data: dict[str, Any]) -> dict[str, Any]:
        print(f"[Mock POST] {url}")
        return {"status": 201}


def fetch_user_data(client: HTTPClientProtocol, user_id: int) -> dict[str, Any]:
    return client.get(f"https://api.dev.io/users/{user_id}")


if __name__ == "__main__":
    print("--- Level 2 ---")
    fh = FileHandler()
    print(f"Is FileHandler Closeable at runtime? {isinstance(fh, Closeable)}")
    fh.close()

    print("\n--- Level 4 ---")
    res = fetch_user_data(MockHTTPClient(), 101)
    print(f"Result: {res}")
