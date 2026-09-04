"""
Basic SQL Aggregations and Filtering in Python.
"""

import sqlite3


def demo_sql_aggregations() -> None:
    conn = sqlite3.connect(":memory:")
    with conn:
        conn.execute("CREATE TABLE sales (id INTEGER PRIMARY KEY, category TEXT, amount REAL)")
        conn.executemany(
            "INSERT INTO sales (category, amount) VALUES (?, ?)",
            [
                ("Electronics", 1200.0),
                ("Electronics", 800.0),
                ("Books", 25.0),
                ("Books", 15.0),
                ("Clothing", 150.0),
            ],
        )

    # SQL GROUP BY and SUM aggregation query
    query = """
        SELECT category, COUNT(*) as total_orders, SUM(amount) as total_revenue
        FROM sales
        GROUP BY category
        HAVING total_revenue > 30.0
        ORDER BY total_revenue DESC
    """

    cursor = conn.execute(query)
    rows = cursor.fetchall()

    print("Category Sales Performance:")
    for cat, count, revenue in rows:
        print(f" Category: {cat:<12} | Orders: {count} | Total Revenue: ${revenue:.2f}")

    conn.close()


if __name__ == "__main__":
    demo_sql_aggregations()
