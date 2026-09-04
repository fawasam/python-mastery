# SQLAlchemy 2.0 ORM (Object-Relational Mapping) in Python

## What You Will Learn
* SQLAlchemy 2.0 Modern `DeclarativeBase` ORM mapping.
* `Mapped` type annotations and `mapped_column()`.
* Working with `Session` context managers.
* ORM relationships (`relationship()`, `ForeignKey`).
* Querying using `session.scalars(select(Model))`.

## Why This Matters
Object-Relational Mapping (ORM) bridges Python objects and SQL relational tables. Instead of writing raw SQL strings or tuple indexing, ORM models let you query and manipulate database records directly as native Python object instances with full type safety.

## Prerequisites
* Classes & Dataclasses (`03_object_oriented_programming/classes_objects`, `03_object_oriented_programming/dataclasses`)
* SQLAlchemy Core (`07_databases/sqlalchemy`)

## Core Concepts

### 1. Modern Declarative Mapping (SQLAlchemy 2.0)
```python
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    orders: Mapped[list["Order"]] = relationship(back_populates="user")

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="orders")
```

### 2. Session Context Manager
```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    user = User(username="alice")
    session.add(user)
    session.commit()
```

## Common Mistakes
* **N+1 Query Problem**: Iterating over relationships in a loop without eager loading (`joinedload` / `selectinload`) causes a separate SQL query for every single row!
* **Accessing lazy-loaded attributes outside session scope**: Raises `DetachedInstanceError`.

## Exercises
See `04_exercises.py` to practice creating linked User and Post ORM models.
