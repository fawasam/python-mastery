"""
Multi-Layer Integration Test: Repository + Service Layer Integration.
"""

import sqlite3


class ProductRepository:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn
        with self.conn:
            self.conn.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL)")

    def add_product(self, name: str, price: float) -> int:
        with self.conn:
            cur = self.conn.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
            return cur.lastrowid

    def get_product(self, product_id: int) -> tuple[int, str, float] | None:
        cur = self.conn.execute("SELECT id, name, price FROM products WHERE id = ?", (product_id,))
        return cur.fetchone()


class InventoryService:
    def __init__(self, repo: ProductRepository) -> None:
        self.repo = repo

    def create_discounted_product(self, name: str, original_price: float, discount_pct: float) -> int:
        discounted_price = round(original_price * (1.0 - discount_pct / 100.0), 2)
        return self.repo.add_product(name, discounted_price)


def test_inventory_service_integration() -> None:
    conn = sqlite3.connect(":memory:")
    repo = ProductRepository(conn)
    service = InventoryService(repo)

    pid = service.create_discounted_product("Gaming Mouse", 100.0, 20.0)
    record = repo.get_product(pid)

    assert record is not None
    assert record[1] == "Gaming Mouse"
    assert record[2] == 80.0
    conn.close()
    print("Multi-layer repository + service integration test passed successfully!")


if __name__ == "__main__":
    test_inventory_service_integration()
