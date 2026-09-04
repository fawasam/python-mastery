"""
Basic Flask App and Test Client Verification.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/api/v1/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "service": "Flask API"})


@app.route("/api/v1/echo", methods=["POST"])
def echo_payload():
    data = request.get_json() or {}
    return jsonify({"received": data}), 201


def test_flask_endpoints() -> None:
    client = app.test_client()

    # GET /health
    res1 = client.get("/api/v1/health")
    assert res1.status_code == 200
    assert res1.get_json()["status"] == "healthy"

    # POST /echo
    res2 = client.post("/api/v1/echo", json={"key": "value"})
    assert res2.status_code == 201
    assert res2.get_json() == {"received": {"key": "value"}}
    print("Flask endpoints and test_client verification passed!")


if __name__ == "__main__":
    test_flask_endpoints()
