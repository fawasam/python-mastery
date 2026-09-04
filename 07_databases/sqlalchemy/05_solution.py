"""
Solutions for SQLAlchemy 2.0 Exercises.
"""

from sqlalchemy import Column, Engine, Integer, MetaData, String, Table, create_engine, select

metadata = MetaData()
items_table = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("sku", String, nullable=False),
)


def get_item_by_sku(engine: Engine, sku: str) -> tuple | None:
    stmt = select(items_table).where(items_table.c.sku == sku)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        return result.fetchone()


if __name__ == "__main__":
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)

    with engine.begin() as conn:
        conn.execute(items_table.insert(), [{"sku": "SKU-1001"}, {"sku": "SKU-1002"}])

    item = get_item_by_sku(engine, "SKU-1001")
    assert item is not None
    assert item.sku == "SKU-1001"
    print(f"Retrieved SKU item: {item.sku}")
