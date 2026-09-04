"""
FastAPI Exercises.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class MathRequest(BaseModel):
    a: float
    b: float


# Exercise 1 (Medium): Build POST /add route handler taking MathRequest and returning {"result": a + b}
@app.post("/add")
def add_numbers(req: MathRequest) -> dict[str, float]:
    raise NotImplementedError("Implement add_numbers")
