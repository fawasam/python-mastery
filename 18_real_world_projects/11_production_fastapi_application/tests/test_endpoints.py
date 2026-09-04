"""
Integration Tests for Enterprise FastAPI Application.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "HEALTHY"


def test_user_creation_flow() -> None:
    payload = {
        "username": "alice_enterprise",
        "email": "alice@enterprise.com",
        "full_name": "Alice Developer"
    }
    res = client.post("/v1/users/", json=payload)
    assert res.status_code == 201
    data = res.json()
    assert data["username"] == "alice_enterprise"
    assert data["id"] == 1
