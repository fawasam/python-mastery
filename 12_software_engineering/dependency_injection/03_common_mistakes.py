"""
Dependency Injection Anti-Patterns: Service Locator Anti-Pattern.
"""

from typing import Any


class ServiceLocator:
    """
    ANTI-PATTERN: Service Locator.
    
    Why: Using a global registry locator inside component methods hides real dependencies
    from class signatures and creates global coupling.
    """
    _services: dict[str, Any] = {}

    @classmethod
    def register(cls, name: str, service: Any) -> None:
        cls._services[name] = service

    @classmethod
    def get(cls, name: str) -> Any:
        return cls._services[name]


class BadReportGenerator:
    """
    MISTAKE: Pulling dependencies out of a hidden global ServiceLocator.
    """
    def generate(self) -> None:
        # Hidden dependency! Signature does not expose dependency on email_service
        email_svc = ServiceLocator.get("email_service")
        email_svc.send_report("Report Content")


if __name__ == "__main__":
    print("Service Locator anti-pattern demonstration module.")
