# Software Engineering Mini Project Architectural Breakdown

## Architectural Highlights

### 1. Single Responsibility Principle (SRP)
- `Task`: Enforces task state transitions (`mark_completed`, `mark_in_progress`).
- `InMemoryTaskRepository`: Handles state storage and retrieval.
- `TaskService`: Orchestrates user actions/use cases.

### 2. Dependency Inversion Principle (DIP)
`TaskService` depends on the `TaskRepository` interface rather than a concrete database driver. Switching from memory to SQLite or PostgreSQL requires zero changes to `TaskService`.

### 3. Clear Layering
Domain business rules are completely shielded from database storage engines and presentation drivers.
