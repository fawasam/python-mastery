"""
Embeddings Basics: Generating TF-IDF Text Vector Embeddings.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def demonstrate_text_embeddings() -> None:
    corpus = [
        "Python is a high-level programming language.",
        "Java is a popular object-oriented language.",
        "Cooking pizza requires flour, cheese, and tomatoes."
    ]

    vectorizer = TfidfVectorizer()
    # Fit and transform corpus into sparse embedding matrix
    embeddings = vectorizer.fit_transform(corpus)

    print("Embedding Matrix Shape (documents x vocab size):", embeddings.shape)

    # Compute pairwise similarity matrix
    sim_matrix = cosine_similarity(embeddings)
    print("\nPairwise Document Similarity Matrix:")
    print(sim_matrix.round(3))


if __name__ == "__main__":
    demonstrate_text_embeddings()
