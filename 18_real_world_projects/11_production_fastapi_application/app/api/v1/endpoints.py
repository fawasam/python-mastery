"""
API V1 Endpoint Controllers.
"""

from fastapi import APIRouter, HTTPException
from app.repositories.user_repository import InMemoryUserRepository
from app.schemas.user import UserCreateSchema, UserResponseSchema
from app.services.user_service import UserService

router = APIRouter(prefix="/v1/users", tags=["Users"])

# Repository Singleton Wiring
_repo = InMemoryUserRepository()
_service = UserService(_repo)


@router.post("/", response_model=UserResponseSchema, status_code=201)

def create_user_endpoint(payload: UserCreateSchema) -> UserResponseSchema:
    try:
        user_db = _service.register_user(payload)
        return UserResponseSchema(
            id=user_db.id,
            username=user_db.username,
            email=user_db.email,
            full_name=user_db.full_name,
            is_active=user_db.is_active
        )
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))
