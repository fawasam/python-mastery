"""
API Documentation Exercises.
"""

from pydantic import BaseModel, Field


# Exercise 1 (Easy): Create Documented Pydantic Schema 'BookSchema'
# Fields:
# - title: str (required, Field description "Book title")
# - pages: int (gt=0, Field description "Page count")
class BookSchema(BaseModel):
    title: str = Field(..., description="Book title")
    pages: int = Field(..., gt=0, description="Page count")
