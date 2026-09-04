"""
Topic: Hello World & Printing Basics
File: 05_solution.py

Official solutions for 04_exercises.py.
"""

def level_1_easy() -> None:
    """Level 1 — Easy Solution"""
    print("Developer Name: Fawaz")
    print("Favorite Language: Python")


def level_2_medium() -> None:
    """Level 2 — Medium Solution"""
    print("Python", "3.12", "Professional", sep=":")


def level_3_hard() -> None:
    """Level 3 — Hard Solution"""
    print("Processing item 1...", end=" -> ")
    print("Processing item 2...", end=" -> ")
    print("Processing item 3...")


def level_4_real_world() -> None:
    """Level 4 — Real World Solution"""
    header = """+----------------------------------+
|      DATA PIPELINE OPERATOR      |
+----------------------------------+"""
    print(header)


if __name__ == "__main__":
    print("--- Level 1 Solution ---")
    level_1_easy()
    
    print("\n--- Level 2 Solution ---")
    level_2_medium()
    
    print("\n--- Level 3 Solution ---")
    level_3_hard()
    
    print("\n--- Level 4 Solution ---")
    level_4_real_world()
