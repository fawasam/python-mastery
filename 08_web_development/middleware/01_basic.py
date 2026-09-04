"""
Basic FastAPI HTTP Middleware Pattern.
"""

import time
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient

app = FastAPI()


@app.middleware("http")
async def add_custom_process_header(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    duration_ms = (time.perf_counter() - start) * 1000
    response.headers["X-Response-Time-MS"] = f"{duration_ms:.2f}"
    return response


@app.get("/api/v1/test")
def sample_endpoint() -> dict[str, str]:
    return {"status": "ok"}


def test_middleware() -> None:
    client = TestClient(app)
    response = client.get("/api/v1/test")

    assert response.status_code == 200
    assert "X-Response-Time-MS" in response.headers
    print(f"Middleware injected X-Response-Time-MS: {response.headers['X-Response-Time-MS']}ms")


if __name__ == "__main__":
    test_middleware()
