# Retrieval-Augmented Generation (RAG) Systems

## What You Will Learn
- What RAG is (combining external document retrieval with LLM generation)
- Document Chunking strategies (overlapping windows)
- Retrieving top-k context passages using vector similarity
- Constructing grounded context prompts to eliminate LLM hallucinations

## Why This Matters
Base LLMs are limited by their static training cutoff dates and lack access to private enterprise knowledge databases. RAG retrieves relevant private context passages at query time and injects them directly into the LLM prompt.

## RAG Architecture

```text
 User Query → [ Vector Store Retrieval ] → Top Relevant Chunks
                                                     ↓
 Grounded Prompt: "Answer query using Context: [Chunks]" → [ LLM ] → Grounded Answer
```

## Examples
See `01_basic.py` and `02_examples.py` for runnable code.

## Exercises
Complete exercises in `04_exercises.py` and check `05_solution.py`.

## Next Topic
Proceed to `../agents/`.
