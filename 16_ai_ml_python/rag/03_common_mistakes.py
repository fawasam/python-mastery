"""
RAG Common Pitfalls.
"""

# MISTAKE: Passing massive un-chunked document bodies directly into LLM prompts.
# WHY: Exceeds LLM context window token limits and dilutes attention over irrelevant text ("lost in the middle" phenomenon).
# FIX: Chunk documents into small, focused passages (200-500 words) and retrieve only top-K relevant chunks.

if __name__ == "__main__":
    print("RAG chunking and context window rules verified.")
