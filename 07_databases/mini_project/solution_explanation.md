# Solution Explanation: E-Commerce Persistence & Transaction Engine

## Architectural Highlights

1. **Declarative ORM Mapping (`DeclarativeBase`, `Mapped`, `mapped_column`)**:
   Uses SQLAlchemy 2.0 type-annotated mappings with cascade rules (`cascade="all, delete-orphan"`).

2. **Atomic Transaction Scope (`session.begin()`)**:
   `session.begin()` guarantees that stock deduction, line item insertion, and customer balance updates execute within a single ACID transaction block. If stock or balance checks fail midway, any uncommitted mutations roll back cleanly.

3. **Repository Pattern (`OrderRepository`)**:
   Decouples database transaction mechanics from high-level business code.
