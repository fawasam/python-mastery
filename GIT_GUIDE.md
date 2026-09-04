# Python Mastery — Git & Version Control Guide

As a professional Python developer, version control with Git is a fundamental daily tool. This guide covers essential Git commands and best practices tailored for Python projects.

---

## 🚀 Basic Git Workflow

```bash
# Initialize a new Git repository
git init

# Check the status of modified and untracked files
git status

# Stage specific files or all changes
git add README.md
git add .

# Commit staged changes with a descriptive message
git commit -m "feat(beginner): complete variables and data types modules"
```

---

## 🌿 Branching & Merging

```bash
# Create and switch to a new feature branch
git checkout -b feature/async-http-client
# Or modern syntax:
git switch -c feature/async-http-client

# Switch back to main branch
git switch main

# Merge feature branch into current branch
git merge feature/async-http-client

# Delete feature branch after merge
git branch -d feature/async-http-client
```

---

## 🔄 Rebase & Stash

```bash
# Rebase feature branch onto latest main
git switch feature/async-http-client
git rebase main

# Temporarily stash uncommitted changes
git stash

# Re-apply stashed changes
git stash pop
```

---

## 📝 Commit Message Standard (Conventional Commits)

Use concise, present-tense, structured commit messages:

- `feat(scope)`: A new feature for the user or codebase.
- `fix(scope)`: A bug fix.
- `docs(scope)`: Documentation only changes.
- `refactor(scope)`: Code change that neither fixes a bug nor adds a feature.
- `test(scope)`: Adding missing tests or correcting existing tests.
- `chore(scope)`: Changes to build process or tooling configuration.

**Example**:
```text
feat(08_web_development): add FastAPI user authentication endpoint with JWT tokens
```

---

## 🙈 `.gitignore` for Python

Always ignore virtual environments, cache files, and environment secrets:
- `.venv/`
- `__pycache__/`
- `.env`
- `.pytest_cache/`
- `.mypy_cache/`
