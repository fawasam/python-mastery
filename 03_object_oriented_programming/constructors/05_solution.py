"""
Topic: Constructor Solutions
File: 05_solution.py
"""
import json
from typing import Any, Self

class Date:
    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_iso(cls, iso_str: str) -> Self:
        parts = iso_str.split("-")
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))


class User:
    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        data = json.loads(json_str)
        return cls(data["username"], data["email"])


class ApiResponse:
    def __init__(self, status_code: int, data: Any = None, error: str | None = None) -> None:
        self.status_code = status_code
        self.data = data
        self.error = error

    @classmethod
    def success(cls, data: Any) -> Self:
        return cls(status_code=200, data=data, error=None)

    @classmethod
    def error(cls, message: str, status_code: int = 400) -> Self:
        return cls(status_code=status_code, data=None, error=message)


if __name__ == "__main__":
    print("--- Level 1 ---")
    d = Date.from_iso("2026-09-04")
    print(f"Date: {d.year}/{d.month}/{d.day}")

    print("\n--- Level 2 ---")
    u = User.from_json('{"username": "alice", "email": "a@dev.io"}')
    print(f"User: {u.username} <{u.email}>")

    print("\n--- Level 4 ---")
    res_ok = ApiResponse.success({"user_id": 101})
    res_err = ApiResponse.error("Invalid input", 422)

    print(f"Success Response: status={res_ok.status_code}, data={res_ok.data}")
    print(f"Error Response:   status={res_err.status_code}, error={res_err.error}")
