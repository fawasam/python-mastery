"""
Solutions for Database Design Exercises.
"""

import sqlite3


def setup_tags_schema(conn: sqlite3.Connection) -> None:
    with conn:
        conn.execute("CREATE TABLE posts (id INTEGER PRIMARY KEY, title TEXT)")
        conn.execute("CREATE TABLE tags (id INTEGER PRIMARY KEY, name TEXT UNIQUE)")
        conn.execute(
            """
            CREATE TABLE post_tags (
                post_id INTEGER,
                tag_id INTEGER,
                PRIMARY KEY (post_id, tag_id),
                FOREIGN KEY (post_id) REFERENCES posts(id),
                FOREIGN KEY (tag_id) REFERENCES tags(id)
            )
        """
        )


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    setup_tags_schema(conn)

    with conn:
        conn.execute("INSERT INTO posts VALUES (1, 'Python Mastery Guide')")
        conn.execute("INSERT INTO tags VALUES (10, 'python')")
        conn.execute("INSERT INTO post_tags VALUES (1, 10)")

    cur = conn.execute(
        """
        SELECT posts.title, tags.name
        FROM posts
        JOIN post_tags ON posts.id = post_tags.post_id
        JOIN tags ON tags.id = post_tags.tag_id
    """
    )
    row = cur.fetchone()
    assert row == ("Python Mastery Guide", "python")
    print(f"Verified Post-Tag relationship: '{row[0]}' tagged with '{row[1]}'")
    conn.close()
