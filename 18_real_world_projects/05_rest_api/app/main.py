"""
FastAPI Application Entrypoint.
"""

from fastapi import FastAPI, HTTPException
from app.models import ItemCreate, ItemResponse

app = FastAPI(title="Production REST API")

items_db: dict[int, ItemResponse] = {}


@app.post("/items/", response_model=ItemResponse, status_code=201)

def create_item(payload: ItemCreate) -> ItemResponse:
    item_id = len(items_db) + 1
    item = ItemResponse(id=item_id, name=payload.name, price=payload.price)
    items_db[item_id] = item
    return item


@app.get("/items/{item_id}", response_model=ItemResponse)

def get_item(item_id: int) -> ItemResponse:
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]
