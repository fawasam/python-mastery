"""
AI/ML Mini Project: Enterprise RAG & AI Agent Engine.
"""

import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class GuardrailSanitizer:
    @staticmethod
    def sanitize(prompt: str) -> str:
        if "override instructions" in prompt.lower():
            raise ValueError("Prompt Injection detected")
        return re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "[REDACTED_SSN]", prompt)


class KnowledgeRetriever:
    def __init__(self, corpus: list[str]) -> None:
        self.corpus = corpus
        self.vectorizer = TfidfVectorizer()
        self.matrix = self.vectorizer.fit_transform(corpus)

    def retrieve(self, query: str, top_k: int = 1) -> str:
        q_vec = self.vectorizer.transform([query])
        sims = cosine_similarity(q_vec, self.matrix)[0]
        best_idx = int(sims.argmax())
        return self.corpus[best_idx]


class AIAgentEngine:
    def __init__(self, retriever: KnowledgeRetriever) -> None:
        self.retriever = retriever

    def process_user_request(self, raw_user_prompt: str) -> str:
        # 1. Sanitize
        clean_prompt = GuardrailSanitizer.sanitize(raw_user_prompt)
        
        # 2. Retrieve Context
        context_passage = self.retriever.retrieve(clean_prompt)
        
        # 3. Formulate Grounded Answer
        return (
            f"--- AI Agent Response ---\n"
            f"Query: {clean_prompt}\n"
            f"Retrieved Context: '{context_passage}'\n"
            f"Grounded Answer: Based on internal documents: {context_passage}"
        )


def main() -> None:
    knowledge_base = [
        "Python 3.12+ introduced powerful performance improvements and improved error messages.",
        "FastAPI is an asynchronous web framework built on Pydantic and Starlette.",
        "RAG systems combine vector search retrieval with large language model generation."
    ]
    
    retriever = KnowledgeRetriever(knowledge_base)
    agent = AIAgentEngine(retriever)

    prompt = "Tell me about Python performance enhancements."
    print("User Prompt:", prompt)
    
    response = agent.process_user_request(prompt)
    print(response)


if __name__ == "__main__":
    main()
