# Relational SQL Fundamentals in Python

## What You Will Learn
* Core Relational SQL statements (`SELECT`, `INSERT`, `UPDATE`, `DELETE`).
* Filtering (`WHERE`, `LIKE`, `IN`, `BETWEEN`).
* Aggregation & Grouping (`COUNT`, `SUM`, `AVG`, `GROUP BY`, `HAVING`).
* Joining tables (`INNER JOIN`, `LEFT JOIN`).

## Why This Matters
SQL (Structured Query Language) is the universal language of relational data storage. Writing clean, efficient SQL queries directly in Python ensures performant data retrieval and transformation without memory overhead.

## Prerequisites
* SQLite Database Integration (`07_databases/sqlite`)

## Core Concepts

### 1. Table Joins
```sql
SELECT orders.id, users.username, orders.amount
FROM orders
INNER JOIN users ON orders.user_id = users.id;
```

### 2. Aggregations & Grouping
```sql
SELECT department, COUNT(*) as emp_count, AVG(salary) as avg_sal
FROM employees
GROUP BY department
HAVING avg_sal > 50000;
```

## Exercises
See `04_exercises.py` to practice constructing SQL aggregation and join queries.
