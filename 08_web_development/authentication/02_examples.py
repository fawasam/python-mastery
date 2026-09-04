"""
FastAPI Header API Key Authentication Dependency.
"""

from fastapi import Depends, FastAPI, HTTPException, Header
from fastapi.testclient import TestClient

app = FastAPI()

VALID_API_KEYS = {"secret_api_key_1001": "AliceCorp"}


def verify_api_key(x_api_key: str = Header(...)) -> str:
    """Dependency verifying X-API-Key request header."""
    if x_api_key not in VALID_API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid or missing X-API-Key header")
    return VALID_API_KEYS[x_api_key]


@app.get("/api/v1/protected")
def protected_endpoint(client_name: str = Depends(verify_api_key)) -> dict[str, str]:
    return {"message": f"Welcome to secure zone, {client_name}"}


def test_api_key_authentication() -> None:
    client = TestClient(app)

    # 1. Unauthenticated request -> 422/401 Missing Header
    res_unauth = client.get("/api/v1/protected")
    assert res_unauth.status_code in (401, 422)

    # 2. Invalid Key -> 401 Unauthorized
    res_invalid = client.get("/api/v1/protected", headers={"X-API-Key": "wrong_key"})
    assert res_invalid.status_code == 401

    # 3. Valid Key -> 200 OK
    res_valid = client.get("/api/v1/protected", headers={"X-API-Key": "secret_api_key_1001"})
    assert res_valid.status_code == 200
    assert "AliceCorp" in res_valid.json()["message"]
    print("API Key header authentication tests passed successfully!")


if __name__ == "__main__":
    test_api_key_authentication()
