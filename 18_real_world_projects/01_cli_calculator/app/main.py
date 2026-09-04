"""
Calculator CLI Main Entrypoint.
"""

from rich.console import Console
import typer
from app.calculator import CalculatorEngine

app = typer.Typer(help="CLI Calculator Application")
console = Console()


@app.command("calc")
def calculate(
    a: float = typer.Argument(..., help="First operand"),
    op: str = typer.Argument(..., help="Operation (+, -, *, /)"),
    b: float = typer.Argument(..., help="Second operand")
) -> None:
    engine = CalculatorEngine()
    try:
        if op == "+":
            res = engine.add(a, b)
        elif op == "-":
            res = engine.subtract(a, b)
        elif op == "*":
            res = engine.multiply(a, b)
        elif op == "/":
            res = engine.divide(a, b)
        else:
            console.print(f"[red]Error: Unsupported operator '{op}'[/red]")
            return
            
        console.print(f"[bold green]Result:[/bold green] {a} {op} {b} = [bold yellow]{res}[/bold yellow]")
    except Exception as err:
        console.print(f"[bold red]Error:[/bold red] {err}")


if __name__ == "__main__":
    app(args=["calc", "10", "+", "20"])
