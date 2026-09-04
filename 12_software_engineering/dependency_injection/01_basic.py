"""
Dependency Injection Basics: Constructor Injection vs Tightly Coupled Code.
"""

from typing import Protocol


class DatabaseClient(Protocol):
    """Abstraction for database interaction."""
    def fetch_user_data(self, user_id: int) -> dict[str, str]:
        ...


class PostgresDatabase:
    """Concrete production database client."""
    def fetch_user_data(self, user_id: int) -> dict[str, str]:
        return {"id": str(user_id), "name": "Real User from DB"}


class MockDatabase:
    """Fake database client for unit testing."""
    def fetch_user_data(self, user_id: int) -> dict[str, str]:
        return {"id": str(user_id), "name": "Mock Test User"}


class UserService:
    """
    Service using Constructor Dependency Injection.
    
    Why: Takes DatabaseClient abstraction via __init__. Can run with PostgresDatabase in production
    and MockDatabase during automated testing without modifying a single line of UserService code!
    """
    def __init__(self, db_client: DatabaseClient) -> None:
        self.db_client = db_client

    def get_user_profile(self, user_id: int) -> str:
        data = self.db_client.fetch_user_data(user_id)
        return f"User Profile: {data['name']} (ID: {data['id']})"


if __name__ == "__main__":
    # Production Wiring
    prod_service = UserService(PostgresDatabase())
    print("Prod execution:", prod_service.get_user_profile(42))
    
    # Test Wiring
    test_service = UserService(MockDatabase())
    print("Test execution:", test_service.get_user_profile(42))
