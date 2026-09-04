"""
Tests for RAG Application Engine.
"""

from app.rag_engine import RAGCore


def test_rag_query() -> None:
    corpus = ["Python 3.12 performance optimization", "JavaScript V8 engine"]
    rag = RAGCore(corpus)
    res = rag.query("Tell me about Python speed")
    assert "Python 3.12 performance optimization" in res
