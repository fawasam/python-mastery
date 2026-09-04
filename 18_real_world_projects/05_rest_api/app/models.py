"""
API Data Schemas.
"""

from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0.0)


class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
