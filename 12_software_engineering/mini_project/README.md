# Mini Project: Clean Architecture Task Management System

## Overview
In this mini project, you will build a clean, layered Task Management system implementing the Repository Pattern, Service Layer, Dependency Injection, and SOLID design principles.

## Architecture
```text
  [ Presentation (main.py) ]
             ↓
  [ Service Layer (TaskService) ]
             ↓
  [ Repository Interface (TaskRepository) ]
             ↓
  [ In-Memory Infrastructure (InMemoryTaskRepository) ]
```

## Objectives
1. Decouple domain logic from infrastructure persistence using the Repository Pattern.
2. Enforce business invariants inside pure dataclass domain entities (`Task`).
3. Inject repository dependencies cleanly into the application service layer.

## How to Run
```bash
python main.py
```
