"""
Advanced Argparse: Subcommands (Git-style CLI).
"""

import argparse


def build_git_cli() -> argparse.ArgumentParser:
    """Build a multi-subcommand CLI tool."""
    parser = argparse.ArgumentParser(prog="mygit", description="Git-style CLI interface")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: init
    init_parser = subparsers.add_parser("init", help="Initialize repository")
    init_parser.add_argument("--bare", action="store_true", help="Create a bare repository")

    # Subcommand: commit
    commit_parser = subparsers.add_parser("commit", help="Record changes")
    commit_parser.add_argument("-m", "--message", required=True, help="Commit message")

    return parser


if __name__ == "__main__":
    parser = build_git_cli()
    
    # Test 'commit' subcommand
    args = parser.parse_args(["commit", "-m", "Initial commit"])
    print(f"Command executed: {args.command}, Message: {args.message}")
