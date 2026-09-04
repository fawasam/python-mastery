"""
Basic OpenAPI Schema Extraction and FastAPI Self-Documentation.
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Documented Catalog API", version="2.0.0")


class CatalogItem(BaseModel):
    name: str = Field(description="Display title of item", examples=["Wireless Mouse"])
    price: float = Field(gt=0, description="Price in USD", examples=[29.99])


@app.post("/api/v1/catalog", summary="Add catalog item", response_description="Saved catalog item")
def add_catalog_item(item: CatalogItem) -> dict[str, str | float]:
    """
    Registers a new product inside the public catalog.
    """
    return {"name": item.name, "price": item.price}


def test_openapi_json_generation() -> None:
    # FastAPI automatically builds an OpenAPI 3.0 JSON schema
    schema = app.openapi()

    assert schema["info"]["title"] == "Documented Catalog API"
    assert schema["info"]["version"] == "2.0.0"
    assert "/api/v1/catalog" in schema["paths"]

    post_spec = schema["paths"]["/api/v1/catalog"]["post"]
    assert post_spec["summary"] == "Add catalog item"
    print("OpenAPI schema auto-generation test passed successfully!")


if __name__ == "__main__":
    test_openapi_json_generation()
