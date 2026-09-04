"""
Advanced Scikit-Learn: Building Feature Scaling & Classifier Pipelines.
"""

from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def run_pipeline_example() -> None:
    X, y = make_classification(n_samples=200, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Construct reusable Scikit-Learn Pipeline
    pipeline = make_pipeline(
        StandardScaler(),
        RandomForestClassifier(n_estimators=50, random_state=42)
    )

    # Fit pipeline on training data (automatically scales features, then trains RF)
    pipeline.fit(X_train, y_train)

    train_score = pipeline.score(X_train, y_train)
    test_score = pipeline.score(X_test, y_test)

    print(f"Train Accuracy: {train_score * 100:.1f}%")
    print(f"Test Accuracy:  {test_score * 100:.1f}%")


if __name__ == "__main__":
    run_pipeline_example()
