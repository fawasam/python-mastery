"""
Typer Basics: Defining CLI commands with type hints.
"""

import typer

app = typer.Typer(help="User management CLI built with Typer.")


@app.command()
def create_user(
    username: str,
    email: str = typer.Option(..., help="User's email address"),
    admin: bool = typer.Option(False, "--admin", "-a", help="Grant administrator privileges"),
) -> None:
    """
    Create a new user account.
    """
    role = "Administrator" if admin else "Standard User"
    typer.echo(f"Created user '{username}' ({email}) with role: {role}")


@app.command()
def delete_user(username: str) -> None:
    """
    Delete a user account by username.
    """
    typer.echo(f"Deleted user '{username}'.")


if __name__ == "__main__":
    # Test typer invocation programmatically
    app(args=["create-user", "alice", "--email", "alice@example.com", "--admin"])
