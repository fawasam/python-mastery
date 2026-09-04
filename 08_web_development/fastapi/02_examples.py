"""
FastAPI Path and Query Parameter Validation with Pydantic.
"""

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

app = FastAPI()


class ProductSchema(BaseModel):
    name: str = Field(..., min_length=2)
    price: float = Field(..., gt=0.0)


@app.get("/items/{item_id}")
def get_item(item_id: int, include_tax: bool = False) -> dict[str, float | int | bool]:
    if item_id > 100:
        raise HTTPException(status_code=404, detail="Item not found")
    base_price = 50.0
    final_price = round(base_price * 1.1, 2) if include_tax else base_price
    return {"item_id": item_id, "price": final_price, "tax_included": include_tax}


def test_fastapi_validation() -> None:
    client = TestClient(app)

    # Test path + query parameters
    res = client.get("/items/5", params={"include_tax": "true"})
    assert res.status_code == 200
    assert res.json()["price"] == 55.0

    # Test 404 HTTPException
    res_404 = client.get("/items/999")
    assert res_404.status_code == 404
    assert res_404.json() == {"detail": "Item not found"}
    print("FastAPI query parameters and HTTPException tests passed!")


if __name__ == "__main__":
    test_fastapi_validation()
