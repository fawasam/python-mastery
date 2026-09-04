"""
Flask Error Handlers and URL Dynamic Parameters.
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource Not Found", "code": 404}), 404


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    if user_id != 1:
        return jsonify({"error": f"User {user_id} does not exist"}), 404
    return jsonify({"id": 1, "username": "alice"})


def test_flask_error_handler() -> None:
    client = app.test_client()

    res_valid = client.get("/users/1")
    assert res_valid.status_code == 200
    assert res_valid.get_json()["username"] == "alice"

    res_invalid = client.get("/users/99")
    assert res_invalid.status_code == 404
    print("Flask dynamic parameters and error handlers passed successfully!")


if __name__ == "__main__":
    test_flask_error_handler()
