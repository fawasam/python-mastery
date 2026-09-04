"""
Tests for REST API.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_and_get_item() -> None:
    res = client.post("/items/", json={"name": "Widget", "price": 19.99})
    assert res.status_code == 201
    data = res.json()
    assert data["name"] == "Widget"

    get_res = client.get(f"/items/{data['id']}")
    assert get_res.status_code == 200
    assert get_res.json()["name"] == "Widget"
