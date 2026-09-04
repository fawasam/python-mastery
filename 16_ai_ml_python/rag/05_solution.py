"""
Solutions: RAG Exercises.
"""


def construct_rag_prompt(context_passages: list[str], question: str) -> str:
    ctx = "\n---\n".join(context_passages)
    return f"Context:\n{ctx}\n\nQuestion: {question}"


if __name__ == "__main__":
    prompt = construct_rag_prompt(["Passage 1 content"], "What is the policy?")
    print("Constructed RAG Prompt:\n", prompt)
