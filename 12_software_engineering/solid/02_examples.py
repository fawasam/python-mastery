"""
SOLID Principles Part 2: Interface Segregation (ISP) & Dependency Inversion (DIP).
"""

from typing import Protocol


# ==========================================
# 4. Interface Segregation Principle (ISP)
# ==========================================
# Instead of one giant interface, split into narrow, specific protocols.

class Printer(Protocol):
    def print_document(self, content: str) -> None:
        ...


class Scanner(Protocol):
    def scan_document(self) -> str:
        ...


class SimplePrinter:
    """Implements ONLY Printer interface; not forced to implement scanning."""
    def print_document(self, content: str) -> None:
        print(f"Printing: {content}")


class MultiFunctionPrinter:
    """Implements both Printer and Scanner interfaces."""
    def print_document(self, content: str) -> None:
        print(f"MFP Printing: {content}")
        
    def scan_document(self) -> str:
        return "Scanned PDF content"


# ==========================================
# 5. Dependency Inversion Principle (DIP)
# ==========================================

class MessageSender(Protocol):
    """High-level abstraction for messaging."""
    def send(self, recipient: str, message: str) -> None:
        ...


class SendersEmailService:
    """Concrete implementation 1."""
    def send(self, recipient: str, message: str) -> None:
        print(f"Sending email to {recipient}: {message}")


class SendersSMSService:
    """Concrete implementation 2."""
    def send(self, recipient: str, message: str) -> None:
        print(f"Sending SMS to {recipient}: {message}")


class NotificationService:
    """
    High-level module depending on MessageSender abstraction, NOT concrete services.
    
    Why: Easy to mock in tests or switch from Email to SMS without changing NotificationService.
    """
    def __init__(self, sender: MessageSender) -> None:
        self.sender = sender

    def notify(self, user: str, msg: str) -> None:
        self.sender.send(user, msg)


if __name__ == "__main__":
    email_notifier = NotificationService(SendersEmailService())
    email_notifier.notify("user@example.com", "Order Shipped!")
    
    sms_notifier = NotificationService(SendersSMSService())
    sms_notifier.notify("+15551234567", "Your OTP is 9876")
