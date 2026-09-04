"""
Scikit-Learn Basics: Train/Test Split, Model Training, and Evaluation.
"""

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def train_and_evaluate_classifier() -> float:
    # 1. Generate synthetic binary classification dataset
    X, y = make_classification(n_samples=500, n_features=4, random_state=42)

    # 2. Split dataset into 80% training and 20% test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Instantiate and train Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # 4. Predict on unseen test set
    y_pred = model.predict(X_test)

    # 5. Compute test accuracy score
    acc = accuracy_score(y_test, y_pred)
    return float(acc)


if __name__ == "__main__":
    accuracy = train_and_evaluate_classifier()
    print(f"Logistic Regression Model Accuracy: {accuracy * 100:.2f}%")
