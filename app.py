from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.post("/add")
def add():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON object required"}), 400

    a = data.get("a")
    b = data.get("b")

    # bool is a subclass of int in Python, so reject it explicitly.
    if (
        isinstance(a, bool)
        or isinstance(b, bool)
        or not isinstance(a, (int, float))
        or not isinstance(b, (int, float))
    ):
        return jsonify({"error": "a and b must be numbers"}), 400

    return jsonify({"result": a + b}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
