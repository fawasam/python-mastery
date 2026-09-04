# AI/ML Mini Project Architectural Breakdown

## Architectural Layers
1. **Safety Guardrails**: Implements string sanitization and PII redaction.
2. **Vector Retrieval Engine**: Uses Scikit-Learn TF-IDF and Cosine Similarity to find relevant context passages.
3. **Agent Orchestration**: Connects prompt sanitization, vector retrieval, and grounded response synthesis into a unified pipeline.
