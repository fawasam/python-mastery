"""
Mini-Project 03: Object-Oriented Library Management System
File: main.py
"""
from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class Transaction:
    transaction_id: str
    member_id: str
    isbn: str
    action: str  # "BORROW" or "RETURN"
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))


class Book:
    def __init__(self, isbn: str, title: str, author: str) -> None:
        self.isbn = isbn
        self.title = title
        self.author = author
        self._is_borrowed = False

    @property
    def is_borrowed(self) -> bool:
        return self._is_borrowed

    def mark_borrowed(self) -> None:
        if self._is_borrowed:
            raise ValueError(f"Book '{self.title}' is already checked out.")
        self._is_borrowed = True

    def mark_returned(self) -> None:
        if not self._is_borrowed:
            raise ValueError(f"Book '{self.title}' is not checked out.")
        self._is_borrowed = False

    def __repr__(self) -> str:
        status = "Borrowed" if self._is_borrowed else "Available"
        return f"Book(ISBN={self.isbn}, '{self.title}' by {self.author} [{status}])"


class Member:
    def __init__(self, member_id: str, name: str, max_limit: int = 3) -> None:
        self.member_id = member_id
        self.name = name
        self.max_limit = max_limit
        self._borrowed_isbns: set[str] = set()

    def can_borrow(self) -> bool:
        return len(self._borrowed_isbns) < self.max_limit

    def borrow_book(self, isbn: str) -> None:
        if not self.can_borrow():
            raise ValueError(f"Member {self.name} has reached borrow limit ({self.max_limit}).")
        self._borrowed_isbns.add(isbn)

    def return_book(self, isbn: str) -> None:
        if isbn in self._borrowed_isbns:
            self._borrowed_isbns.remove(isbn)


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self._catalog: dict[str, Book] = {}
        self._members: dict[str, Member] = {}
        self._transactions: list[Transaction] = []

    def add_book(self, book: Book) -> None:
        self._catalog[book.isbn] = book
        print(f"📖 Added to catalog: {book.title}")

    def register_member(self, member: Member) -> None:
        self._members[member.member_id] = member
        print(f"👤 Registered member: {member.name} ({member.member_id})")

    def checkout_book(self, member_id: str, isbn: str) -> Transaction:
        if member_id not in self._members:
            raise KeyError(f"Member ID {member_id} not registered.")
        if isbn not in self._catalog:
            raise KeyError(f"Book ISBN {isbn} not found in catalog.")

        member = self._members[member_id]
        book = self._catalog[isbn]

        book.mark_borrowed()
        member.borrow_book(isbn)

        tx = Transaction(
            transaction_id=f"TX-{len(self._transactions) + 1:04d}",
            member_id=member_id,
            isbn=isbn,
            action="BORROW",
        )
        self._transactions.append(tx)
        print(f"✅ Checkout Success: {member.name} -> '{book.title}'")
        return tx

    def return_book(self, member_id: str, isbn: str) -> Transaction:
        member = self._members[member_id]
        book = self._catalog[isbn]

        book.mark_returned()
        member.return_book(isbn)

        tx = Transaction(
            transaction_id=f"TX-{len(self._transactions) + 1:04d}",
            member_id=member_id,
            isbn=isbn,
            action="RETURN",
        )
        self._transactions.append(tx)
        print(f"🔄 Return Success: '{book.title}' returned by {member.name}")
        return tx


if __name__ == "__main__":
    print("--- Library Management System Demo ---")
    lib = Library("City Central Library")

    b1 = Book("978-0132350884", "Clean Code", "Robert C. Martin")
    b2 = Book("978-0201616224", "The Pragmatic Programmer", "Andy Hunt")
    lib.add_book(b1)
    lib.add_book(b2)

    m1 = Member("M001", "Alice Johnson")
    lib.register_member(m1)

    # Perform transactions
    lib.checkout_book("M001", "978-0132350884")
    lib.return_book("M001", "978-0132350884")
