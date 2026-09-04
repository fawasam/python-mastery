"""
Topic: Set Fundamentals & Mathematical Operations
File: 01_basic.py
"""

def demonstrate_set_operations() -> None:
    # 1. Automatic Deduplication
    raw_user_ids = [101, 102, 101, 103, 102, 104]
    unique_user_ids = set(raw_user_ids)
    print(f"Raw IDs:    {raw_user_ids}")
    print(f"Unique IDs: {unique_user_ids}")

    # 2. Set Algebraic Operations
    frontend_skills = {"HTML", "CSS", "JavaScript", "TypeScript"}
    backend_skills = {"Python", "JavaScript", "TypeScript", "SQL"}

    print("\n--- Skill Set Algebra ---")
    # Union (all skills combined)
    all_skills = frontend_skills | backend_skills
    print(f"Union (Frontend | Backend): {all_skills}")

    # Intersection (common skills)
    fullstack_overlap = frontend_skills & backend_skills
    print(f"Intersection (Frontend & Backend): {fullstack_overlap}")

    # Difference (Frontend only)
    frontend_only = frontend_skills - backend_skills
    print(f"Difference (Frontend - Backend): {frontend_only}")


if __name__ == "__main__":
    demonstrate_set_operations()
