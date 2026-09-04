# Database Design & Normalization in Python

## What You Will Learn
* Principles of Relational Database Schema Design.
* Primary Keys, Foreign Keys, Unique Constraints, and Indexes.
* Normalization Forms (1NF, 2NF, 3NF).
* Designing One-to-One, One-to-Many, and Many-to-Many entity relationships.
* Migrations & Schema Evolution.

## Why This Matters
Good database design is the bedrock of application performance and data integrity. Properly normalized schemas eliminate duplicate data, prevent insertion/update anomalies, and enforce relational constraints at the database level.

## Prerequisites
* Relational SQL (`07_databases/sql`)
* ORM (`07_databases/orm`)

## Core Concepts

### Entity Relationship Mapping
- **1-to-1**: User <-> UserProfile
- **1-to-Many**: Department <-> Employees
- **Many-to-Many**: Student <-> Course (Requires Junction Table `student_courses`!)

### Junction Table Pattern (Many-to-Many)
```sql
CREATE TABLE students (id INT PRIMARY KEY, name TEXT);
CREATE TABLE courses (id INT PRIMARY KEY, title TEXT);

-- Junction Table
CREATE TABLE student_courses (
    student_id INT REFERENCES students(id),
    course_id INT REFERENCES courses(id),
    PRIMARY KEY (student_id, course_id)
);
```

## Exercises
See `04_exercises.py` to practice designing Many-to-Many junction tables.
