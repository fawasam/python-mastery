"""
RAG Basics: Document Chunking and Overlapping Sliding Windows.
"""


def chunk_document_text(text: str, chunk_size: int = 50, overlap: int = 10) -> list[str]:
    """
    Split long document text into overlapping character chunks.
    
    Why: Overlapping preserves semantic context across chunk boundaries.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += (chunk_size - overlap)
    return chunks


if __name__ == "__main__":
    doc = "Retrieval-Augmented Generation (RAG) empowers LLMs with private knowledge bases by retrieving relevant document passages."
    chunks = chunk_document_text(doc, chunk_size=40, overlap=10)
    
    print(f"Generated {len(chunks)} chunks:")
    for idx, c in enumerate(chunks, 1):
        print(f"Chunk #{idx}: '{c}'")
