"""
SQLAlchemy 2.0 Core Filtering, Joins, and Aggregations.
"""

from sqlalchemy import Column, Float, ForeignKey, Integer, MetaData, String, Table, create_engine, func, select

engine = create_engine("sqlite:///:memory:", echo=False)
metadata = MetaData()

departments = Table(
    "departments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)

employees = Table(
    "employees",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("salary", Float, nullable=False),
    Column("dept_id", Integer, ForeignKey("departments.id")),
)


def demo_sqlalchemy_aggregations() -> None:
    metadata.create_all(engine)

    with engine.begin() as conn:
        conn.execute(departments.insert(), [{"id": 1, "name": "Engineering"}, {"id": 2, "name": "Sales"}])
        conn.execute(
            employees.insert(),
            [
                {"name": "Alice", "salary": 90000.0, "dept_id": 1},
                {"name": "Bob", "salary": 110000.0, "dept_id": 1},
                {"name": "Charlie", "salary": 65000.0, "dept_id": 2},
            ],
        )

    # Join + Group By + Avg Aggregate
    j = employees.join(departments, employees.c.dept_id == departments.c.id)
    stmt = (
        select(departments.c.name.label("dept"), func.avg(employees.c.salary).label("avg_salary"))
        .select_from(j)
        .group_by(departments.c.name)
    )

    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print(f"Department: {row.dept:<12} | Avg Salary: ${row.avg_salary:.2f}")


if __name__ == "__main__":
    demo_sqlalchemy_aggregations()
