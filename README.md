# Python Mastery: Absolute Beginner → Advanced → Production Engineer

Welcome to **Python Mastery**, a comprehensive, production-grade learning repository built directly inside your editor. This repository takes you step-by-step from writing your first line of Python code to designing distributed, asynchronous, production-quality systems and building AI/ML applications.

---

## 🗺 Learning Progression Roadmap

```text
    ┌─────────────────────────────────────────┐
    │          01. ABSOLUTE BEGINNER          │
    │  Syntax, Variables, Types, Loops, Funcs │
    └────────────────────┬────────────────────┘
                         │
                         ▼
    ┌─────────────────────────────────────────┐
    │             02. CORE PYTHON             │
    │ Comprehensions, Generators, Decorators  │
    └────────────────────┬────────────────────┘
                         │
                         ▼
    ┌─────────────────────────────────────────┐
    │     03. OBJECT-ORIENTED PROGRAMMING     │
    │  Classes, Inheritance, Dunder Methods   │
    └────────────────────┬────────────────────┘
                         │
                         ▼
    ┌─────────────────────────────────────────┐
    │        04. INTERMEDIATE PYTHON          │
    │   Type Hints, Protocols, GC & Memory    │
    └────────────────────┬────────────────────┘
                         │
                         ▼
    ┌─────────────────────────────────────────┐
    │     05. ERROR HANDLING & DEBUGGING      │
    │ Logging, Custom Exceptions, Defensive   │
    └────────────────────┬────────────────────┘
                         │
                         ▼
    ┌─────────────────────────────────────────┐
    │               06. TESTING               │
    │ Pytest, Fixtures, Mocking, Integration  │
    └────────────────────┬────────────────────┘
                         │
                         ▼
    ┌─────────────────────────────────────────┐
    │     07. DATABASES & 08. WEB DEV         │
    │   SQLite, SQLAlchemy, REST, FastAPI     │
    └────────────────────┬────────────────────┘
                         │
                         ▼
    ┌─────────────────────────────────────────┐
    │ 09. ASYNC & 10. CONCURRENCY/PARALLELISM │
    │ Asyncio, Coroutines, Multiprocessing    │
    └────────────────────┬────────────────────┘
                         │
                         ▼
    ┌─────────────────────────────────────────┐
    │ 11. PERFORMANCE & 12. SOFTWARE ENG.     │
    │ Profiling, Caching, SOLID, Clean Arch   │
    └────────────────────┬────────────────────┘
                         │
                         ▼
    ┌─────────────────────────────────────────┐
    │   13. CLI, 14. AUTO, 15. DATA & 16. AI  │
    │ Typer, Automation, Pandas, RAG, Agents  │
    └────────────────────┬────────────────────┘
                         │
                         ▼
    ┌─────────────────────────────────────────┐
    │ 17. ADVANCED, 18. PROJECTS & 19-20 PREP │
    │   Metaclasses, Real Projects, Interviews│
    └─────────────────────────────────────────┘
```

---

## 📂 Repository Structure

```text
python-mastery/
├── README.md                          # Repository Master Documentation
├── LEARNING_GUIDE.md                  # Pedagogical Study Guide & Methodologies
├── PROGRESS.md                        # Progress Tracking Checklists
├── GIT_GUIDE.md                       # Git Workflows for Python Engineering
├── pyproject.toml                     # Ruff, Pytest, and Mypy Configurations
├── requirements.txt                   # Dependency Declarations
├── .gitignore                         # Python VCS Exclusion Rules
├── 01_beginner/                       # 17 Beginner Topics + Mini Project
├── 02_core_python/                    # 15 Core Language Mechanics + Mini Project
├── 03_object_oriented_programming/    # 11 OOP Topics + Mini Project
├── 04_intermediate_python/            # 11 Intermediate Topics + Mini Project
├── 05_error_handling_debugging/       # 6 Debugging Topics + Mini Project
├── 06_testing/                        # 7 Testing Topics + Mini Project
├── 07_databases/                      # SQL & ORM Engineering + Mini Project
├── 08_web_development/                # REST, FastAPI, Auth + Mini Project
├── 09_async_python/                   # Asyncio, Coroutines + Mini Project
├── 10_concurrency_parallelism/        # Threading & Multiprocessing + Mini Project
├── 11_performance/                    # Profiling & Optimization + Mini Project
├── 12_software_engineering/           # SOLID, Clean Architecture + Mini Project
├── 13_cli_development/                # Typer & Rich CLI + Mini Project
├── 14_automation/                     # Web, Files & System Automation + Mini Project
├── 15_data_processing/                # NumPy & Pandas + Mini Project
├── 16_ai_ml_python/                   # Scikit-Learn, RAG & AI Agents + Mini Project
├── 17_advanced_python/                # Metaclasses, AST, Bytecode + Mini Project
├── 18_real_world_projects/            # 11 Production Engineering Applications
├── 19_interview_preparation/          # 200+ Q&As, Coding Problems & Systems
└── 20_challenges/                     # Rated Coding Challenges (⭐ to ⭐⭐⭐⭐⭐)
```

---

## ⚡ How to Run Code & Setup Virtual Environment

1. **Initialize Environment**:
   ```bash
   cd python-mastery
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Execute Any Lesson Script**:
   ```bash
   python 01_beginner/01_hello_world/01_basic.py
   ```

3. **Run Tests**:
   ```bash
   pytest
   ```

4. **Run Linter & Type Checker**:
   ```bash
   ruff check .
   mypy .
   ```

---

## 📚 Study Strategy & Workflow

For each topic folder:
1. **Read `README.md`**: Grasp the concept, syntax, and real-world usage.
2. **Run `01_basic.py`**: Understand fundamental code execution line-by-line.
3. **Run `02_examples.py`**: See realistic production examples.
4. **Inspect `03_common_mistakes.py`**: Avoid common pitfalls and antipatterns.
5. **Solve `04_exercises.py`**: Implement solutions for Levels 1–4.
6. **Verify against `05_solution.py`**: Compare your code with idiomatic Python solutions.

---

## 🐙 GitHub Repository & Git Setup

- **GitHub Repository URL**: `https://github.com/fawasam/python-mastery.git`

### Initializing Git and Pushing to GitHub

If you are pushing this repository to GitHub for the first time:

```bash
# Navigate into the project directory
cd python-mastery

# Initialize Git repository (if not already initialized)
git init

# Rename default branch to main
git branch -M main

# Add remote origin
git remote add origin https://github.com/fawasam/python-mastery.git

# Stage all files
git add .

# Create initial commit
git commit -m "feat: initial commit for Python Mastery learning repository"

# Push to GitHub main branch
git push -u origin main
```

---

Happy Coding! 🚀
