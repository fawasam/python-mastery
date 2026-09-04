# Database Transactions & ACID Principles in Python

## What You Will Learn
* Understanding **ACID** properties (Atomicity, Consistency, Isolation, Durability).
* Transaction management in SQLite and SQLAlchemy (`commit()`, `rollback()`, `SAVEPOINT`).
* Preventing race conditions and partial updates.
* Transaction isolation levels (`READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`).

## Why This Matters
Financial processing, order fulfillment, and multi-step data transformations require transaction guarantees. If an error occurs midway through a 3-step operation, atomicity ensures all previous modifications are rolled back, leaving the database in a consistent state.

## Prerequisites
* Relational SQL & SQLite (`07_databases/sqlite`, `07_databases/sql`)

## Core Concepts

### ACID Principles
- **Atomicity**: All operations in a transaction succeed or all fail together ("All-or-Nothing").
- **Consistency**: Database transitions from one valid schema state to another.
- **Isolation**: Concurrent transactions execute without interfering with each other's uncommitted state.
- **Durability**: Committed data survives system crashes or outages.

## Exercises
See `04_exercises.py` to practice implementing atomic transaction rollback handlers.
