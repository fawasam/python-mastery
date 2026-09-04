"""
RAG Application Entrypoint.
"""

from app.rag_engine import RAGCore


def main() -> None:
    docs = [
        "Company Policy: PTO allowance is 20 days per year.",
        "Company Policy: Remote work requires team lead approval."
    ]
    rag = RAGCore(docs)
    answer = rag.query("What is the remote work policy?")
    print("RAG Application Result:\n", answer)


if __name__ == "__main__":
    main()
