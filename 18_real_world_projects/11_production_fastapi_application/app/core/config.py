"""
Application Global Settings.
"""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    app_name: str = "Production Enterprise API"
    env: str = os.getenv("ENV", "development")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///:memory:")


settings = Settings()
