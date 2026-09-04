"""
Structured Custom Exception Hierarchy Example for an API Framework.
"""


class APIException(Exception):
    """Root exception for REST API errors."""

    status_code: int = 500

    def __init__(self, message: str, payload: dict[str, str] | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.payload = payload or {}

    def to_dict(self) -> dict[str, str | int | dict[str, str]]:
        return {"error": self.message, "status_code": self.status_code, "details": self.payload}


class NotFoundError(APIException):
    status_code = 404


class UnauthorizedError(APIException):
    status_code = 401


def get_user_profile(user_id: int) -> dict[str, str]:
    if user_id != 1:
        raise NotFoundError("User not found", payload={"user_id": str(user_id)})
    return {"id": "1", "username": "alice"}


if __name__ == "__main__":
    try:
        get_user_profile(99)
    except APIException as err:
        print(f"API Error Caught (HTTP {err.status_code}): {err.to_dict()}")
