"""
Topic: Unpacking Iterables in Function Calls
File: 02_examples.py
"""

def connect_db(host: str, port: int, user: str, dbname: str) -> str:
    return f"postgres://{user}@{host}:{port}/{dbname}"


if __name__ == "__main__":
    connection_tuple = ("db.internal", 5432, "app_user", "analytics_db")
    # Unpacking positional arguments from tuple using *
    conn_str1 = connect_db(*connection_tuple)
    print(f"Unpacked Tuple Call: {conn_str1}")

    connection_dict = {
        "host": "replica.internal",
        "port": 5432,
        "user": "read_user",
        "dbname": "reporting",
    }
    # Unpacking keyword arguments from dictionary using **
    conn_str2 = connect_db(**connection_dict)
    print(f"Unpacked Dict Call:  {conn_str2}")
