"""
RAG Engine.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class RAGCore:
    def __init__(self, corpus: list[str]) -> None:
        self.corpus = corpus
        self.vectorizer = TfidfVectorizer()
        self.doc_embeddings = self.vectorizer.fit_transform(corpus)

    def query(self, user_query: str) -> str:
        q_vec = self.vectorizer.transform([user_query])
        sims = cosine_similarity(q_vec, self.doc_embeddings)[0]
        best_idx = int(sims.argmax())
        retrieved = self.corpus[best_idx]
        return f"[Grounded RAG Answer from Passage: '{retrieved}']"
