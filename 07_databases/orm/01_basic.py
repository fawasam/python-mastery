"""
Basic SQLAlchemy 2.0 ORM Declarative Model and Session CRUD.
"""

from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    role: Mapped[str] = mapped_column(String(20), default="user")

    def __repr__(self) -> str:
        return f"<Account id={self.id} email='{self.email}' role='{self.role}'>"


def demo_orm_crud() -> None:
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)

    # 1. Create (Insert)
    with Session(engine) as session:
        acc1 = Account(email="alice@dev.io", role="admin")
        acc2 = Account(email="bob@dev.io")
        session.add_all([acc1, acc2])
        session.commit()

    # 2. Read (Select)
    with Session(engine) as session:
        # 2.0 style scalars selection
        stmt = select(Account).where(Account.role == "admin")
        admin_acc = session.scalars(stmt).first()
        print(f"Queried Admin Account: {admin_acc}")

    # 3. Update & Delete
    with Session(engine) as session:
        acc = session.scalars(select(Account).where(Account.email == "bob@dev.io")).one()
        acc.role = "manager"  # ORM automatically tracks attribute mutations!
        session.commit()

        updated_acc = session.scalars(select(Account).where(Account.email == "bob@dev.io")).one()
        print(f"Updated Bob Account: {updated_acc}")


if __name__ == "__main__":
    demo_orm_crud()
