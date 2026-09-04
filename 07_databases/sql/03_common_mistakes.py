"""
Common Mistakes in Relational SQL Queries.
"""


# MISTAKE 1: Forgetting WHERE clause in UPDATE or DELETE statements
def mistake_unfiltered_delete() -> None:
    # DANGER: Executing "DELETE FROM users" without WHERE clause deletes ALL RECORDS in the entire table!
    pass


if __name__ == "__main__":
    print("Always double check WHERE clauses before executing UPDATE or DELETE SQL operations!")
