"""
Basic Many-to-Many Relational Schema with Junction Table.
"""

import sqlite3


def setup_many_to_many_schema() -> None:
    conn = sqlite3.connect(":memory:")
    with conn:
        # Entities
        conn.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT)")
        conn.execute("CREATE TABLE courses (id INTEGER PRIMARY KEY, code TEXT)")

        # Junction / Bridge Table
        conn.execute(
            """
            CREATE TABLE student_courses (
                student_id INTEGER,
                course_id INTEGER,
                enrolled_at TEXT DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (student_id, course_id),
                FOREIGN KEY (student_id) REFERENCES students(id),
                FOREIGN KEY (course_id) REFERENCES courses(id)
            )
        """
        )

        # Seed data
        conn.executemany("INSERT INTO students VALUES (?, ?)", [(1, "Alice"), (2, "Bob")])
        conn.executemany("INSERT INTO courses VALUES (?, ?)", [(101, "CS101"), (102, "MATH201")])
        conn.executemany("INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)", [(1, 101), (1, 102), (2, 101)])

    # Query student courses via 3-way join
    query = """
        SELECT students.name, courses.code
        FROM students
        JOIN student_courses ON students.id = student_courses.student_id
        JOIN courses ON courses.id = student_courses.course_id
        ORDER BY students.name
    """

    print("Student Course Enrollments:")
    for student, course in conn.execute(query):
        print(f" - {student} enrolled in {course}")

    conn.close()


if __name__ == "__main__":
    setup_many_to_many_schema()
