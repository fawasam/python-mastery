"""
Advanced Embeddings: Semantic Document Search Engine.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


class SemanticSearchEngine:
    """Simple in-memory vector search engine using NearestNeighbors."""
    def __init__(self) -> None:
        self.vectorizer = TfidfVectorizer()
        self.documents: list[str] = []
        self.nn_model = NearestNeighbors(n_neighbors=2, metric="cosine")

    def fit(self, documents: list[str]) -> None:
        self.documents = documents
        embeddings = self.vectorizer.fit_transform(documents)
        self.nn_model.fit(embeddings)

    def search(self, query: str, top_k: int = 2) -> list[tuple[str, float]]:
        query_vec = self.vectorizer.transform([query])
        distances, indices = self.nn_model.kneighbors(query_vec, n_neighbors=top_k)
        
        results = []
        for dist, idx in zip(distances[0], indices[0]):
            similarity = 1.0 - float(dist)
            results.append((self.documents[idx], similarity))
            
        return results


if __name__ == "__main__":
    docs = [
        "FastAPI is a modern web framework for building APIs with Python.",
        "PostgreSQL is a powerful open-source relational database system.",
        "Pytest makes writing simple and scalable unit tests in Python easy."
    ]

    engine = SemanticSearchEngine()
    engine.fit(docs)

    matches = engine.search("How to build web APIs in Python?", top_k=1)
    print("Top Search Match:")
    print(f"Document: '{matches[0][0]}' (Score: {matches[0][1]:.4f})")
