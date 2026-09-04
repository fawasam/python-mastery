"""
Solutions: Embeddings Exercises.
"""

from typing import Any
from sklearn.feature_extraction.text import TfidfVectorizer


def create_vector_embeddings(corpus: list[str]) -> Any:
    vectorizer = TfidfVectorizer()
    return vectorizer.fit_transform(corpus)


if __name__ == "__main__":
    matrix = create_vector_embeddings(["doc one", "doc two"])
    print("Embedded matrix shape:", matrix.shape)
