"""
NumPy for AI/ML Basics: Cosine Similarity and Vector Normalization.
"""

import numpy as np


def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    Calculate cosine similarity between two vector embeddings.
    
    Returns float score between -1.0 and +1.0.
    """
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0
        
    return float(dot_product / (norm_v1 * norm_v2))


if __name__ == "__main__":
    # Synthetic 4-dimensional vector embeddings
    emb_a = np.array([0.1, 0.8, 0.4, 0.0])
    emb_b = np.array([0.2, 0.7, 0.5, 0.1])
    emb_c = np.array([-0.9, 0.0, 0.1, -0.8])

    sim_ab = cosine_similarity(emb_a, emb_b)
    sim_ac = cosine_similarity(emb_a, emb_c)

    print(f"Cosine Similarity (A, B - Similar): {sim_ab:.4f}")
    print(f"Cosine Similarity (A, C - Dissimilar): {sim_ac:.4f}")
