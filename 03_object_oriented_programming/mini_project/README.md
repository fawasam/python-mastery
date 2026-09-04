# Mini-Project 03: Object-Oriented Library Management System

## Project Overview
Build a clean, robust, Object-Oriented Library Management System that models books, members, transactions, and library catalog services using OOP principles (Classes, Encapsulation, Composition, Inheritance, and Dataclasses).

## Core Domain Models
1. `Book`: Domain entity representing a library book item (`isbn`, `title`, `author`, `is_borrowed`).
2. `Member`: Encapsulated domain model representing a library member (`member_id`, `name`, `borrowed_books`).
3. `Transaction`: Dataclass tracking borrowing and returning records with timestamp.
4. `Library`: Service class managing book inventory and member interactions.

## How to Run
```bash
python 03_object_oriented_programming/mini_project/main.py
```
