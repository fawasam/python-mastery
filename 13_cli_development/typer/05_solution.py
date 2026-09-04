"""
Solutions: Typer Exercises.
"""

import typer

app = typer.Typer()


@app.command("version")
def show_version() -> None:
    """Print application version."""
    typer.echo("v1.0.0")


@app.command("info")
def show_info() -> None:
    """Print application info."""
    typer.echo("Typer application info")


def build_version_app() -> typer.Typer:
    return app


if __name__ == "__main__":
    test_app = build_version_app()
    test_app(args=["version"])
