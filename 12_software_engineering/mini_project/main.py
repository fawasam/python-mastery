"""
Software Engineering Mini Project: Clean Task Management System.

Demonstrates SOLID principles, Clean Architecture layering, Repository Pattern, and DI.
"""

from dataclasses import dataclass, field
from enum import Enum, auto
import uuid


# --- DOMAIN LAYER ---

class TaskStatus(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()


@dataclass
class Task:
    """Pure domain entity containing business rules."""
    title: str
    description: str
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: TaskStatus = TaskStatus.PENDING

    def mark_in_progress(self) -> None:
        if self.status == TaskStatus.COMPLETED:
            raise ValueError("Cannot move completed task back to in-progress")
        self.status = TaskStatus.IN_PROGRESS

    def mark_completed(self) -> None:
        self.status = TaskStatus.COMPLETED


# --- INFRASTRUCTURE REPOSITORY INTERFACE ---

class TaskRepository:
    """Repository Protocol interface defining data access contracts."""
    def save(self, task: Task) -> None:
        raise NotImplementedError

    def find_by_id(self, task_id: str) -> Task | None:
        raise NotImplementedError

    def list_all(self) -> list[Task]:
        raise NotImplementedError


class InMemoryTaskRepository(TaskRepository):
    """In-Memory infrastructure implementation of TaskRepository."""
    def __init__(self) -> None:
        self._tasks: dict[str, Task] = {}

    def save(self, task: Task) -> None:
        self._tasks[task.task_id] = task

    def find_by_id(self, task_id: str) -> Task | None:
        return self._tasks.get(task_id)

    def list_all(self) -> list[Task]:
        return list(self._tasks.values())


# --- APPLICATION SERVICE LAYER ---

class TaskService:
    """
    Application Service layer encapsulating use-cases.
    Relies on TaskRepository via Dependency Injection.
    """
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def create_task(self, title: str, description: str) -> Task:
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        task = Task(title=title, description=description)
        self.repository.save(task)
        return task

    def complete_task(self, task_id: str) -> Task:
        task = self.repository.find_by_id(task_id)
        if not task:
            raise KeyError(f"Task {task_id} not found")
        task.mark_completed()
        self.repository.save(task)
        return task

    def get_task_summary(self) -> dict[str, int]:
        all_tasks = self.repository.list_all()
        return {
            "total": len(all_tasks),
            "completed": sum(1 for t in all_tasks if t.status == TaskStatus.COMPLETED),
            "pending": sum(1 for t in all_tasks if t.status == TaskStatus.PENDING),
        }


def main() -> None:
    print("=== Clean Architecture Task Management System ===")
    repo = InMemoryTaskRepository()
    service = TaskService(repo)

    t1 = service.create_task("Fix Security Vulnerabilities", "Patch dependencies in pyproject.toml")
    t2 = service.create_task("Refactor Database Layer", "Implement Repository pattern for PostgreSQL")

    print(f"Created task: '{t1.title}' (ID: {t1.task_id[:8]})")
    print(f"Created task: '{t2.title}' (ID: {t2.task_id[:8]})")

    service.complete_task(t1.task_id)
    print(f"\nCompleted task '{t1.title}'. Status: {t1.status.name}")

    summary = service.get_task_summary()
    print("\nTask System Summary:", summary)


if __name__ == "__main__":
    main()
