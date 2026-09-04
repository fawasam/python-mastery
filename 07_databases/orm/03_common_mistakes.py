"""
Common Mistakes in SQLAlchemy ORM.
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class DummyItem(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(primary_key=True)


# MISTAKE 1: Accessing lazy-loaded attributes after closing the session
def mistake_detached_instance() -> None:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        item = DummyItem(id=1)
        session.add(item)
        session.commit()
        # Session scope closes here! 'item' becomes detached!


if __name__ == "__main__":
    mistake_detached_instance()
    print("Always access required ORM fields while the Session context is active or eager load them!")
