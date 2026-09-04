# NumPy for Machine Learning & Neural Networks

## What You Will Learn
- Vectorized operations for ML feature matrices ($X$) and target vectors ($y$)
- Computing matrix dot products, inner products, and norms
- Standardizing and scaling feature matrices ($\mu = 0, \sigma = 1$)
- Cosine similarity computation between vector embeddings

## Why This Matters
All modern AI/ML frameworks (PyTorch, TensorFlow, Scikit-Learn) represent datasets and neural network parameters as multidimensional NumPy-like tensor arrays.

## Core Equations

### Cosine Similarity
$$\text{Cosine Similarity}(\vec{a}, \vec{b}) = \frac{\vec{a} \cdot \vec{b}}{\|\vec{a}\| \|\vec{b}\|}$$

### Standard Scaling (Z-Score)
$$Z = \frac{X - \mu}{\sigma}$$

## Examples
See `01_basic.py` and `02_examples.py` for runnable code.

## Exercises
Complete exercises in `04_exercises.py` and check solutions in `05_solution.py`.

## Next Topic
Proceed to `../pandas/`.
