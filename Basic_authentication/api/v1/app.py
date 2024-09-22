#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize `auth` based on AUTH_TYPE environment variable
auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type == "auth":
    auth = Auth()  # Create an instance of Auth

# `before_request` to apply authentication checks
@app.before_request
def before_request_func():
    """Before each request, apply authentication logic."""
    # Do nothing if `auth` is None
    if auth is None:
        return

    # Excluded paths
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']

    # Check if the request path requires authentication
    if not auth.require_auth(request.path, excluded_paths):
        return

    # Check for missing Authorization header
    if auth.authorization_header(request) is None:
        abort(401)

    # Check if current user is None (for now, it will always be None)
    if auth.current_user(request) is None:
        abort(403)


# Error Handlers
@app.errorhandler(401)
def unauthorized_error(error):
    """ Unauthorized error """
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)