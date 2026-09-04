"""
Flask Exercises.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


# Exercise 1 (Medium): Create GET /square?n=5 returning jsonify({"square": 25})
@app.route("/square", methods=["GET"])
def compute_square():
    raise NotImplementedError("Implement compute_square")
