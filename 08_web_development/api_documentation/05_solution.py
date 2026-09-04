"""
Solutions for API Documentation Exercises.
"""

from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    title: str = Field(..., description="Book title")
    pages: int = Field(..., gt=0, description="Page count")


if __name__ == "__main__":
    schema = BookSchema.model_json_schema()
    assert "title" in schema["properties"]
    assert "pages" in schema["properties"]
    print("Documented BookSchema JSON schema test passed successfully!")
