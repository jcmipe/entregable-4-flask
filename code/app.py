from flask import Flask, Response, jsonify

GREETING_MESSAGE = "Hola, esta es la aplicación Flask del Entregable 4."

app = Flask(__name__)


@app.get("/")
def home() -> Response:
    return jsonify(message=GREETING_MESSAGE)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
