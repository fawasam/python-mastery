"""
Configuration Basics: Fallback Hierarchy (CLI > Env > Defaults).
"""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AppConfig:
    host: str
    port: int
    debug: bool


def load_config(cli_host: str | None = None, cli_port: int | None = None) -> AppConfig:
    """
    Load configuration adhering to the strict precedence hierarchy:
    CLI Argument > Environment Variable > Hardcoded Default.
    """
    host = cli_host or os.getenv("APP_HOST") or "127.0.0.1"
    
    env_port = os.getenv("APP_PORT")
    port = cli_port or (int(env_port) if env_port else 8000)
    
    debug = os.getenv("APP_DEBUG", "false").lower() in ("true", "1", "yes")
    
    return AppConfig(host=host, port=port, debug=debug)


if __name__ == "__main__":
    # Test loading defaults
    cfg_default = load_config()
    print("Default config loaded:", cfg_default)
    
    # Test CLI override
    cfg_cli = load_config(cli_host="0.0.0.0", cli_port=9090)
    print("CLI-overridden config loaded:", cfg_cli)
