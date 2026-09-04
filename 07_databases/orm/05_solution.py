"""
Solutions for SQLAlchemy ORM Exercises.
"""

from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="pending")


def get_pending_tasks_count(session: Session) -> int:
    stmt = select(Task).where(Task.status == "pending")
    tasks = session.scalars(stmt).all()
    return len(tasks)


if __name__ == "__main__":
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        session.add_all(
            [
                Task(title="Task A", status="pending"),
                Task(title="Task B", status="completed"),
                Task(title="Task C", status="pending"),
            ]
        )
        session.commit()

        count = get_pending_tasks_count(session)
        assert count == 2
        print(f"Pending tasks count: {count}")
