from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "testing github actions"

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "version": "1.0.0",
        "service": "mcp-test-app"
    })

@app.route("/api/info")
def info():
    return jsonify({
        "app": "MCP Test Application",
        "version": "1.0.0",
        "environment": os.getenv("ENVIRONMENT", "development"),
        "port": 5000
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)

