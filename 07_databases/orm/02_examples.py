"""
SQLAlchemy 2.0 ORM One-to-Many Relationships and Joined Eager Loading.
"""

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, joinedload, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    books: Mapped[list["Book"]] = relationship(back_populates="author", cascade="all, delete-orphan")


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    author: Mapped["Author"] = relationship(back_populates="books")


def demo_orm_relationships() -> None:
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        author = Author(
            name="J.R.R. Tolkien",
            books=[
                Book(title="The Hobbit"),
                Book(title="The Fellowship of the Ring"),
            ],
        )
        session.add(author)
        session.commit()

    # Query with joinedload eager loading to eliminate N+1 query problem
    with Session(engine) as session:
        stmt = select(Author).options(joinedload(Author.books)).where(Author.name == "J.R.R. Tolkien")
        retrieved_author = session.scalars(stmt).unique().one()

        print(f"Author: {retrieved_author.name}")
        for b in retrieved_author.books:
            print(f" - Book: {b.title}")


if __name__ == "__main__":
    demo_orm_relationships()
