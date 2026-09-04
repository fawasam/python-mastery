"""
Resource Ownership Authorization Check (Preventing BOLA / IDOR).
"""


class Document:
    def __init__(self, doc_id: int, owner_id: int, content: str) -> None:
        self.doc_id = doc_id
        self.owner_id = owner_id
        self.content = content


def read_document_content(doc: Document, requesting_user_id: int, is_admin: bool = False) -> str:
    # Fail fast if requesting user is neither the resource owner nor an admin
    if not is_admin and doc.owner_id != requesting_user_id:
        raise PermissionError(
            f"User {requesting_user_id} is forbidden from accessing Document {doc.doc_id} owned by User {doc.owner_id}"
        )
    return doc.content


if __name__ == "__main__":
    doc1 = Document(doc_id=101, owner_id=1, content="Confidential Financial Report")

    # Owner access -> Allowed
    print(f"Owner read: {read_document_content(doc1, requesting_user_id=1)}")

    # Admin access -> Allowed
    print(f"Admin read: {read_document_content(doc1, requesting_user_id=99, is_admin=True)}")

    # Unauthorized User 2 access -> Forbidden!
    try:
        read_document_content(doc1, requesting_user_id=2)
    except PermissionError as err:
        print(f"BOLA / IDOR Protection caught violation: {err}")
