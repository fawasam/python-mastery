"""
Main Application Bootstrap.
"""

from fastapi import FastAPI
from app.api.v1.endpoints import router as user_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    docs_url="/docs"
)

app.include_router(user_router)


@app.get("/health")

def health_check() -> dict[str, str]:
    return {"status": "HEALTHY", "environment": settings.env}
