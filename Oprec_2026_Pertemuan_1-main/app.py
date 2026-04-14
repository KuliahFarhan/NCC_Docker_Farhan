from flask import Flask, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/health")
def health():
    app.logger.info("Health endpoint accessed")
    return jsonify({"status": "ok"}), 200

@app.route("/")
def home():
    app.logger.info("Homepage accessed")
    return "Hello from Flask Docker", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)