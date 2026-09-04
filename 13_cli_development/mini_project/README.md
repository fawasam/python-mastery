# Mini Project: Multi-Feature CLI Utility (`pytask`)

## Overview
In this mini project, you will build `pytask`—a multi-command task automation CLI using `typer`, `rich`, and structured JSON storage.

## Features
- `pytask add "Task description"`: Add new pending task.
- `pytask list`: Render tasks in a styled `rich` table.
- `pytask complete <task_id>`: Mark a task as completed.

## Running the CLI
```bash
python main.py add "Refactor FastAPI services"
python main.py list
```
