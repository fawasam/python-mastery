"""
Tests for Auth System.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_login_and_protected_route() -> None:
    res = client.post("/login", json={"username": "admin", "password": "secret123"})
    assert res.status_code == 200
    token = res.json()["access_token"]

    dash_res = client.get("/admin/dashboard", headers={"Authorization": f"Bearer {token}"})
    assert dash_res.status_code == 200
    assert "Welcome Admin" in dash_res.json()["message"]
