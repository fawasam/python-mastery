# Mini Project: E-Commerce Persistence & Transaction Engine

## Overview
This mini project builds a complete persistence layer for an e-commerce platform using SQLAlchemy 2.0 ORM.

It demonstrates:
1. **Relational Database Design**: 1-to-Many and Many-to-Many relationships (`User`, `Product`, `Order`, `OrderItem`).
2. **ACID Transaction Management**: Multi-step order creation with stock deduction and atomic rollback on failure.
3. **Session & Repository Pattern**: Clean encapsulation of database queries.

## Running the Project
```bash
python main.py
```
