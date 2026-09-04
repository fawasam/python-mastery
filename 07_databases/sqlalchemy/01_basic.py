"""
Basic SQLAlchemy 2.0 Core Table Declaration and Querying.
"""

from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine, select

# Create in-memory SQLite engine
engine = create_engine("sqlite:///:memory:", echo=False)
metadata = MetaData()

# Declare table metadata
products_table = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("category", String, nullable=False),
)


def run_sqlalchemy_core_demo() -> None:
    metadata.create_all(engine)

    # Insert data using engine.begin() transaction block
    with engine.begin() as conn:
        conn.execute(
            products_table.insert(),
            [
                {"name": "Laptop", "category": "Electronics"},
                {"name": "Monitor", "category": "Electronics"},
                {"name": "Desk Chair", "category": "Furniture"},
            ],
        )

    # Query data using 2.0 select() construct
    stmt = select(products_table.c.id, products_table.c.name).where(products_table.c.category == "Electronics")

    with engine.connect() as conn:
        result = conn.execute(stmt)
        print("Electronics Products:")
        for row in result:
            print(f" - ID: {row.id} | Name: {row.name}")


if __name__ == "__main__":
    run_sqlalchemy_core_demo()
