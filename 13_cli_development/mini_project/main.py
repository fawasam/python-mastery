"""
CLI Development Mini Project: Task Automation CLI Tool (pytask).
"""

import json
from pathlib import Path
from rich.console import Console
from rich.table import Table
import typer

app = typer.Typer(help="pytask: Terminal Task Management System")
console = Console()

STORAGE_FILE = Path(__file__).parent / "tasks_db.json"


def load_tasks() -> list[dict[str, str]]:
    if not STORAGE_FILE.exists():
        return []
    try:
        with open(STORAGE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_tasks(tasks: list[dict[str, str]]) -> None:
    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


@app.command("add")
def add_task(title: str = typer.Argument(..., help="Task title")) -> None:
    """Add a new task."""
    tasks = load_tasks()
    task_id = str(len(tasks) + 1)
    tasks.append({"id": task_id, "title": title, "status": "PENDING"})
    save_tasks(tasks)
    console.print(f"[bold green]✓[/bold green] Task '{title}' added (ID: {task_id}).")


@app.command("list")
def list_tasks() -> None:
    """List all saved tasks."""
    tasks = load_tasks()
    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return

    table = Table("ID", "Title", "Status")
    for t in tasks:
        status_color = "green" if t["status"] == "COMPLETED" else "yellow"
        table.add_row(t["id"], t["title"], f"[{status_color}]{t['status']}[/{status_color}]")
        
    console.print(table)


@app.command("complete")
def complete_task(task_id: str = typer.Argument(..., help="Task ID to mark complete")) -> None:
    """Mark a task complete by ID."""
    tasks = load_tasks()
    found = False
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "COMPLETED"
            found = True
            break
            
    if found:
        save_tasks(tasks)
        console.print(f"[bold green]✓[/bold green] Task {task_id} marked as COMPLETED.")
    else:
        console.print(f"[bold red]✗[/bold red] Task ID {task_id} not found.", err=True)


if __name__ == "__main__":
    # Test CLI sequence
    app(args=["add", "Learn Typer CLI Development"])
    app(args=["list"])
    app(args=["complete", "1"])
    app(args=["list"])
