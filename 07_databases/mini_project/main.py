"""
E-Commerce Persistence & Transaction Engine using SQLAlchemy 2.0 ORM.
"""

from typing import Sequence
from sqlalchemy import Float, ForeignKey, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, joinedload, mapped_column, relationship


# 1. DECLARATIVE MODEL BASE
class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    balance: Mapped[float] = mapped_column(Float, default=0.0)

    orders: Mapped[list["Order"]] = relationship(back_populates="customer")


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    sku: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    total_amount: Mapped[float] = mapped_column(Float, default=0.0)

    customer: Mapped["Customer"] = relationship(back_populates="orders")
    line_items: Mapped[list["OrderLineItem"]] = relationship(back_populates="order", cascade="all, delete-orphan")


class OrderLineItem(Base):
    __tablename__ = "order_line_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"))
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)

    order: Mapped["Order"] = relationship(back_populates="line_items")
    item: Mapped["Item"] = relationship()


# 2. TRANSACTION REPOSITORY
class OrderRepository:
    def __init__(self, engine) -> None:
        self.engine = engine

    def place_order(self, customer_id: int, cart_items: list[tuple[int, int]]) -> int:
        """
        Atomic transaction: Deducts stock, creates Order & LineItems, and debits customer balance.
        Rolls back completely if stock or funds are insufficient.
        """
        with Session(self.engine) as session:
            with session.begin():  # Begins explicit ACID transaction block
                customer = session.get(Customer, customer_id)
                if not customer:
                    raise ValueError(f"Customer {customer_id} not found")

                order = Order(customer_id=customer.id)
                total_cost = 0.0

                for item_id, qty in cart_items:
                    item = session.get(Item, item_id)
                    if not item or item.stock < qty:
                        raise ValueError(f"Insufficient stock for item ID {item_id}")

                    # Deduct stock
                    item.stock -= qty
                    line_cost = item.price * qty
                    total_cost += line_cost

                    line_item = OrderLineItem(item_id=item.id, quantity=qty, unit_price=item.price)
                    order.line_items.append(line_item)

                if customer.balance < total_cost:
                    raise ValueError(f"Insufficient customer balance: Required ${total_cost:.2f}")

                customer.balance -= total_cost
                order.total_amount = total_cost
                session.add(order)
                session.flush()
                return order.id


if __name__ == "__main__":
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)

    # Seed data
    with Session(engine) as session:
        c1 = Customer(name="Alice", balance=500.0)
        i1 = Item(sku="LAPTOP-01", price=200.0, stock=5)
        i2 = Item(sku="MOUSE-01", price=25.0, stock=10)
        session.add_all([c1, i1, i2])
        session.commit()

    repo = OrderRepository(engine)

    print("--- Placing Order 1 (Successful) ---")
    order_id = repo.place_order(customer_id=1, cart_items=[(1, 1), (2, 2)])  # 200 + 50 = 250
    print(f"Order #{order_id} placed successfully!")

    # Verify updated database state
    with Session(engine) as session:
        c = session.get(Customer, 1)
        print(f"Customer Balance after Order 1: ${c.balance:.2f} (Expected $250.00)")
        item1 = session.get(Item, 1)
        print(f"Laptop stock remaining: {item1.stock} (Expected 4)")

    print("\n--- Placing Order 2 (Should Rollback due to Excessive Quantity) ---")
    try:
        repo.place_order(customer_id=1, cart_items=[(1, 10)])  # Stock is only 4!
    except ValueError as err:
        print(f"Caught Transaction Rollback: {err}")

    # Verify state was untouched by failed transaction
    with Session(engine) as session:
        item1 = session.get(Item, 1)
        print(f"Laptop stock after rolled-back transaction: {item1.stock} (Guaranteed 4!)")
