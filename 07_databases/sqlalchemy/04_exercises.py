"""
SQLAlchemy 2.0 Exercises.
"""

from sqlalchemy import Column, Integer, MetaData, String, Table, Engine, select

metadata = MetaData()
items_table = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("sku", String, nullable=False),
)


# Exercise 1 (Medium): Select Item by SKU
# Write get_item_by_sku(engine: Engine, sku: str) -> tuple | None
# Executes SQLAlchemy select statement and returns single row tuple or None.
def get_item_by_sku(engine: Engine, sku: str) -> tuple | None:
    raise NotImplementedError("Implement get_item_by_sku using SQLAlchemy 2.0 select()")
