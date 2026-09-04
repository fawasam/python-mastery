"""
Standard REST API Response envelope structures.
"""

from typing import Any, Generic, TypeVar

T = TypeVar("T")


class APIResponseEnvelope(Generic[T]):
    """Standardized API Response wrapper."""

    def __init__(self, data: T | None = None, error: str | None = None, status_code: int = 200) -> None:
        self.data = data
        self.error = error
        self.status_code = status_code

    def to_dict(self) -> dict[str, Any]:
        return {
            "success": self.status_code < 400,
            "data": self.data,
            "error": self.error,
        }


if __name__ == "__main__":
    success_resp = APIResponseEnvelope(data={"id": 1, "name": "Alice"}, status_code=200)
    print(f"Success Envelope: {success_resp.to_dict()}")

    error_resp = APIResponseEnvelope(error="Resource not found", status_code=404)
    print(f"Error Envelope  : {error_resp.to_dict()}")
