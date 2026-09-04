"""
Pydantic Schema Examples for Interactive Swagger UI Documentation.
"""

from pydantic import BaseModel, ConfigDict, Field


class UserProfileResponse(BaseModel):
    id: int = Field(description="Unique internal user identifier", examples=[1001])
    username: str = Field(description="Unique username", examples=["alice_smith"])
    is_active: bool = Field(default=True, description="Account status flag")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1001,
                "username": "alice_smith",
                "is_active": True,
            }
        }
    )


if __name__ == "__main__":
    schema = UserProfileResponse.model_json_schema()
    print(f"Generated Pydantic Schema Properties: {list(schema['properties'].keys())}")
    assert "username" in schema["properties"]
