"""
Solutions for Flask Exercises.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/square", methods=["GET"])
def compute_square():
    raw_n = request.args.get("n", "0")
    try:
        val = float(raw_n)
        return jsonify({"square": val**2}), 200
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


if __name__ == "__main__":
    client = app.test_client()
    res = client.get("/square?n=5")
    assert res.status_code == 200
    assert res.get_json() == {"square": 25.0}
    print("Flask /square endpoint exercise solution passed!")
