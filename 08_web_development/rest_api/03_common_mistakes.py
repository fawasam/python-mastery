"""
Common Mistakes in REST API Design.
"""


# MISTAKE 1: Verbs in URI paths
def mistake_verb_in_path() -> None:
    # BAD REST DESIGN: POST /getUserById?id=5 or GET /deleteUser/5
    # GOOD REST DESIGN: GET /users/5 or DELETE /users/5
    pass


if __name__ == "__main__":
    print("Use nouns for REST endpoints (/users, /orders) and HTTP verbs (GET, POST, DELETE) for actions!")
