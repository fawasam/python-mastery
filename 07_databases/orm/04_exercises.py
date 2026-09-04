"""
SQLAlchemy ORM Exercises.
"""

from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="pending")


# Exercise 1 (Medium): Create and query pending tasks
# Write get_pending_tasks_count(session: Session) -> int
# Queries and returns count of Task records where status == "pending".
def get_pending_tasks_count(session: Session) -> int:
    raise NotImplementedError("Implement get_pending_tasks_count")
