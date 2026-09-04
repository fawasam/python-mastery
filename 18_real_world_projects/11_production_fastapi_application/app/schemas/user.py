"""
User Pydantic Data Contracts.
"""

from pydantic import BaseModel, EmailStr, Field


class UserCreateSchema(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    full_name: str


class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    is_active: bool
