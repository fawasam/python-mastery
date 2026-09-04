"""
Clean Code Basics: Comparing Dirty Code vs Clean Code.

This file demonstrates guard clauses, meaningful naming, and function single-responsibility.
"""


# --- DIRTY VERSION ---
def p(u, a, b):
    # What does p do? What are u, a, b?
    if u is not None:
        if u.is_active:
            if a > 0:
                if u.balance >= a:
                    u.balance -= a
                    if b:
                        u.send_receipt()
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


# --- CLEAN VERSION ---

class User:
    """Represents a user account in the system."""
    def __init__(self, name: str, is_active: bool, balance: float) -> None:
        self.name = name
        self.is_active = is_active
        self.balance = balance

    def send_receipt(self) -> None:
        """Simulate sending transaction receipt."""
        print(f"Receipt sent to {self.name}.")


def process_payment(user: User | None, amount: float, notify_user: bool = True) -> bool:
    """
    Process payment for a user account using guard clauses to reduce nesting.
    
    Why: Early returns (guard clauses) keep the happy path unindented and readable.
    """
    # Guard clauses: check edge conditions and exit early
    if user is None or not user.is_active:
        return False
        
    if amount <= 0 or user.balance < amount:
        return False
        
    # Main logic path (clean & unindented)
    user.balance -= amount
    
    if notify_user:
        user.send_receipt()
        
    return True


if __name__ == "__main__":
    alice = User(name="Alice", is_active=True, balance=150.0)
    success = process_payment(user=alice, amount=50.0, notify_user=True)
    print(f"Payment successful: {success}, Alice remaining balance: ${alice.balance:.2f}")
