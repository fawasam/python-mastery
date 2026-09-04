"""
Basic FastAPI Application and TestClient Verification.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI(title="Basic FastAPI App")


class UserCreate(BaseModel):
    username: str
    email: str


@app.get("/api/v1/ping")
def ping() -> dict[str, str]:
    return {"message": "pong"}


@app.post("/api/v1/users", status_code=201)
def create_user(user: UserCreate) -> dict[str, str]:
    return {"id": "USR-101", "username": user.username, "email": user.email}


def test_fastapi_endpoints() -> None:
    client = TestClient(app)

    # Test GET /ping
    res_ping = client.get("/api/v1/ping")
    assert res_ping.status_code == 200
    assert res_ping.json() == {"message": "pong"}

    # Test POST /users
    res_user = client.post("/api/v1/users", json={"username": "alice", "email": "alice@dev.io"})
    assert res_user.status_code == 201
    assert res_user.json()["username"] == "alice"
    print("FastAPI basic routes and TestClient verification passed!")


if __name__ == "__main__":
    test_fastapi_endpoints()
