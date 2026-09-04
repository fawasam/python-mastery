"""
Tests for Blog Backend API.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_and_fetch_blog_post() -> None:
    payload = {"title": "Python 3.14 Released", "slug": "python-314", "body": "Exciting new features!"}
    res = client.post("/posts/", json=payload)
    assert res.status_code == 201
    
    get_res = client.get("/posts/python-314")
    assert get_res.status_code == 200
    assert get_res.json()["title"] == "Python 3.14 Released"
