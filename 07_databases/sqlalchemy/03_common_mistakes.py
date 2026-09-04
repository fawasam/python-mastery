"""
Common Mistakes in SQLAlchemy 2.0 Core.
"""

from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine, select

engine = create_engine("sqlite:///:memory:", echo=False)
metadata = MetaData()
users = Table("users", metadata, Column("id", Integer, primary_key=True), Column("name", String))
metadata.create_all(engine)


# MISTAKE 1: Executing queries directly on Engine instance in 2.0
def mistake_engine_execute() -> None:
    # DANGER: engine.execute() is REMOVED in SQLAlchemy 2.0!
    # Query MUST be executed using a Connection context manager!
    pass


# GOOD PRACTICE: Connect via Engine and execute
def good_connection_execute() -> None:
    with engine.connect() as conn:
        result = conn.execute(select(users))
        _ = result.fetchall()


if __name__ == "__main__":
    good_connection_execute()
    print("SQLAlchemy 2.0 connection query executed successfully!")
