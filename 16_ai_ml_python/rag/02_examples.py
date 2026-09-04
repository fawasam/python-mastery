"""
Advanced RAG: Grounded Context Prompt Construction and Generation.
"""

from dataclasses import dataclass
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@dataclass
class RAGPipeline:
    """In-memory RAG pipeline combining TF-IDF retrieval with grounded context prompting."""
    knowledge_base: list[str]

    def _retrieve_top_k(self, query: str, k: int = 1) -> list[str]:
        vectorizer = TfidfVectorizer()
        matrix = vectorizer.fit_transform(self.knowledge_base + [query])
        
        query_vec = matrix[-1]
        doc_matrix = matrix[:-1]
        
        similarities = cosine_similarity(query_vec, doc_matrix)[0]
        top_idx = similarities.argsort()[-k:][::-1]
        
        return [self.knowledge_base[i] for i in top_idx]

    def answer_query(self, query: str) -> str:
        retrieved_passages = self._retrieve_top_k(query, k=1)
        context = "\n".join(retrieved_passages)

        # Grounded RAG Prompt Construction
        grounded_prompt = (
            f"Use ONLY the following context passages to answer the user's question.\n"
            f"Context:\n{context}\n\n"
            f"Question: {query}\n"
            f"Answer:"
        )

        # Simulated grounded LLM response
        return f"[LLM Grounded Output based on Context passage: '{context}']"


if __name__ == "__main__":
    docs = [
        "Company policy: All employees receive 25 paid vacation days per calendar year.",
        "Company policy: Remote work is permitted up to 3 days per week with manager approval.",
        "Office hours: The main headquarters building is open from 8:00 AM to 6:00 PM."
    ]

    rag = RAGPipeline(knowledge_base=docs)
    answer = rag.answer_query("How many vacation days do employees get?")
    print("RAG Grounded Response:\n", answer)
