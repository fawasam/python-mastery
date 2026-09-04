# Flask Web Framework in Python

## What You Will Learn
* Microframework architecture with Flask.
* Defining routes with `@app.route()`.
* Handling request objects (`request.args`, `request.get_json()`).
* Returning JSON responses with `jsonify()`.
* Testing Flask apps using `app.test_client()`.

## Why This Matters
Flask is a lightweight, battle-tested WSGI web framework widely used for microservices, quick prototypes, and traditional server-rendered applications.

## Prerequisites
* HTTP & REST (`08_web_development/http`, `08_web_development/rest_api`)

## Core Concepts

### Basic Flask App & Route Handling
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/v1/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "Guest")
    return jsonify({"message": f"Hello, {name}!"})
```

## Exercises
See `04_exercises.py` to practice creating Flask endpoints.
