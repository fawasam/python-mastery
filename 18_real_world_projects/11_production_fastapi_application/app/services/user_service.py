"""
User Application Service Layer.
"""

from app.models.user import UserModelDB
from app.repositories.user_repository import UserRepositoryInterface
from app.schemas.user import UserCreateSchema


class UserService:
    def __init__(self, repo: UserRepositoryInterface) -> None:
        self.repo = repo

    def register_user(self, payload: UserCreateSchema) -> UserModelDB:
        existing = self.repo.find_by_username(payload.username)
        if existing:
            raise ValueError(f"Username '{payload.username}' already registered.")
            
        user = UserModelDB(
            username=payload.username,
            email=payload.email,
            full_name=payload.full_name,
            is_active=True
        )
        return self.repo.save(user)
