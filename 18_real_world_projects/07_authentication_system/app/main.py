"""
Authentication API Entrypoint.
"""

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from app.auth import create_token, verify_token

app = FastAPI(title="Authentication & Authorization System")


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/login")

def login(req: LoginRequest) -> dict[str, str]:
    if req.username == "admin" and req.password == "secret123":
        token = create_token(user_id="usr_1001", role="admin")
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid username or password")


@app.get("/admin/dashboard")

def admin_dashboard(authorization: str = Header(...)) -> dict[str, str]:
    token = authorization.replace("Bearer ", "")
    payload = verify_token(token)
    if not payload or payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Forbidden: Admin access required")
    return {"message": f"Welcome Admin {payload['sub']}!"}
