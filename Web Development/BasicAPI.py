import flask
from flask import Flask, jsonify, request
from platform import python_version, system

# Create a flask app which takes the "__name__" variable
app = Flask(__name__)

# Example Route
@app.route("/api/stats")
def getStats():
    return jsonify({"response": 69})

# Returns the version of flask, python and the type of os it runs on
@app.route("/version")
def getVerStats():
    return jsonify({"flask-version": flask.__version__, "python-version": python_version(), "os": system()})

# Handles 404 Not found routes
@app.errorhandler(404)
def _404Handler(err):
    return jsonify({"error-code": 404, "error-response": str(err).replace("requested URL", f"requested URL '{request.path}'"), "response": "Invalid Route."})

# Starts the Flask Server
if __name__ == "__main__":
    app.run()