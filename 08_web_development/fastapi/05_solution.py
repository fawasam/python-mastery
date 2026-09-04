"""
Solutions for FastAPI Exercises.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI()


class MathRequest(BaseModel):
    a: float
    b: float


@app.post("/add")
def add_numbers(req: MathRequest) -> dict[str, float]:
    return {"result": req.a + req.b}


if __name__ == "__main__":
    client = TestClient(app)
    res = client.post("/add", json={"a": 15.5, "b": 4.5})
    assert res.status_code == 200
    assert res.json() == {"result": 20.0}
    print("FastAPI POST /add exercise solution passed successfully!")
