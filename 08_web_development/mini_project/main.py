"""
Task Management REST Microservice with FastAPI.
"""

import time
from typing import Any
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

app = FastAPI(
    title="Task Manager REST Microservice",
    version="1.0.0",
    description="Production-grade FastAPI task management backend with API Key authentication.",
)

# 1. IN-MEMORY DATABASE & SECRETS
DB_TASKS: dict[int, dict[str, Any]] = {}
NEXT_TASK_ID = 1
VALID_KEYS = {"secret_key_1001": "TechLead"}


# 2. SCHEMAS
class TaskCreateSchema(BaseModel):
    title: str = Field(..., min_length=2, description="Title of task", example="Implement OAuth2")
    priority: str = Field(default="medium", description="Priority level (low, medium, high)", example="high")


class TaskResponseSchema(BaseModel):
    id: int = Field(description="Unique task ID", example=1)
    title: str
    priority: str
    completed: bool = False


# 3. AUTHENTICATION DEPENDENCY
def verify_api_key(x_api_key: str = Header(..., description="API Access Key Header")) -> str:
    if x_api_key not in VALID_KEYS:
        raise HTTPException(status_code=401, detail="Invalid or missing X-API-Key header")
    return VALID_KEYS[x_api_key]


# 4. MIDDLEWARE
@app.middleware("http")
async def process_time_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    duration_ms = (time.perf_counter() - start) * 1000
    response.headers["X-Process-Time-MS"] = f"{duration_ms:.2f}"
    return response


# 5. ROUTES
@app.post(
    "/api/v1/tasks",
    response_model=TaskResponseSchema,
    status_code=201,
    summary="Create Task",
    response_description="Created task details",
)
def create_task(task: TaskCreateSchema, user_name: str = Depends(verify_api_key)) -> dict[str, Any]:
    global NEXT_TASK_ID
    task_id = NEXT_TASK_ID
    NEXT_TASK_ID += 1

    record = {"id": task_id, "title": task.title, "priority": task.priority, "completed": False}
    DB_TASKS[task_id] = record
    return record


@app.get("/api/v1/tasks", response_model=list[TaskResponseSchema], summary="List Tasks")
def list_tasks(user_name: str = Depends(verify_api_key)) -> list[dict[str, Any]]:
    return list(DB_TASKS.values())


# 6. TEST SUITE VERIFICATION
def test_task_service_endpoints() -> None:
    client = TestClient(app)
    headers = {"X-API-Key": "secret_key_1001"}

    # Create task
    res_create = client.post("/api/v1/tasks", json={"title": "Setup CI/CD Pipeline", "priority": "high"}, headers=headers)
    assert res_create.status_code == 201
    assert res_create.json()["title"] == "Setup CI/CD Pipeline"
    assert "X-Process-Time-MS" in res_create.headers

    # List tasks
    res_list = client.get("/api/v1/tasks", headers=headers)
    assert res_list.status_code == 200
    assert len(res_list.json()) == 1

    print("FastAPI Task Management Microservice verification passed successfully!")


if __name__ == "__main__":
    test_task_service_endpoints()
