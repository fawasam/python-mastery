"""
Clean Architecture Basics: Domain Entities, Repositories, and Service Layer.
"""

from dataclasses import dataclass
from typing import Protocol


# ==========================================
# 1. DOMAIN LAYER (Pure Business Entities)
# ==========================================

@dataclass
class Account:
    account_id: str
    balance: float
    is_active: bool

    def withdraw(self, amount: float) -> None:
        """Domain business rule."""
        if not self.is_active:
            raise ValueError("Account is inactive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount


# ==========================================
# 2. INFRASTRUCTURE LAYER ABSTRACTIONS (Repository)
# ==========================================

class AccountRepository(Protocol):
    def get_by_id(self, account_id: str) -> Account | None:
        ...

    def save(self, account: Account) -> None:
        ...


# Concrete Repository (In-Memory Implementation)
class InMemoryAccountRepository:
    def __init__(self) -> None:
        self._accounts: dict[str, Account] = {}

    def get_by_id(self, account_id: str) -> Account | None:
        return self._accounts.get(account_id)

    def save(self, account: Account) -> None:
        self._accounts[account.account_id] = account


# ==========================================
# 3. SERVICE LAYER (Use Case Orchestration)
# ==========================================

class BankingService:
    """
    Application Service layer encapsulating use-case logic.
    
    Why: Coordinates domain entities and infrastructure repositories without exposing DB specifics.
    """
    def __init__(self, repo: AccountRepository) -> None:
        self.repo = repo

    def withdraw_funds(self, account_id: str, amount: float) -> Account:
        account = self.repo.get_by_id(account_id)
        if account is None:
            raise KeyError(f"Account {account_id} not found")

        # Delegate business rule execution to domain entity
        account.withdraw(amount)
        
        # Persist updated state
        self.repo.save(account)
        return account


if __name__ == "__main__":
    repo = InMemoryAccountRepository()
    repo.save(Account(account_id="ACC-001", balance=500.0, is_active=True))
    
    service = BankingService(repo)
    updated_acc = service.withdraw_funds("ACC-001", 150.0)
    print(f"Withdrawal complete. Remaining balance: ${updated_acc.balance:.2f}")
