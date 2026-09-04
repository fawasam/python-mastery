"""
Advanced Typer: Nested Subcommands and Rich Integration.
"""

from rich.console import Console
from rich.table import Table
import typer

app = typer.Typer()
db_app = typer.Typer(help="Database administration subcommands.")
app.add_typer(db_app, name="db")

console = Console()


@db_app.command("status")
def db_status() -> None:
    """Show current database connections table."""
    table = Table("Database", "Status", "Connections")
    table.add_row("Primary PG", "[green]ONLINE[/green]", "15")
    table.add_row("Redis Cache", "[green]ONLINE[/green]", "42")
    console.print(table)


if __name__ == "__main__":
    app(args=["db", "status"])
