"""
User Repository Data Access Layer.
"""

from typing import Protocol
from app.models.user import UserModelDB


class UserRepositoryInterface(Protocol):
    def save(self, user: UserModelDB) -> UserModelDB:
        ...

    def find_by_username(self, username: str) -> UserModelDB | None:
        ...


class InMemoryUserRepository:
    def __init__(self) -> None:
        self._db: dict[int, UserModelDB] = {}
        self._counter = 0

    def save(self, user: UserModelDB) -> UserModelDB:
        if not user.id:
            self._counter += 1
            user.id = self._counter
        self._db[user.id] = user
        return user

    def find_by_username(self, username: str) -> UserModelDB | None:
        for u in self._db.values():
            if u.username == username:
                return u
        return None
