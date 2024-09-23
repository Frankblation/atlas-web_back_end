#!/usr/bin/env python3
"""
App initialization and request filtering for authentication.
"""
from os import getenv
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from api.v1.views import app_views
from api.v1.auth.auth import Auth  # Import Auth class

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize `auth` based on AUTH_TYPE environment variable
auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type == "auth":
    auth = Auth()

# Error Handlers


@app.errorhandler(404)
def not_found(error):
    """404 Not Found handler"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_error(error):
    """401 Unauthorized handler"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error):
    """403 Forbidden handler"""
    return jsonify({"error": "Forbidden"}), 403

# Before each request, apply the authentication logic


@app.before_request
def before_request_func():
    """Apply authentication logic before handling each request."""
    if auth is None:
        return  # No authentication needed

    # List of excluded paths (including `/status`)
    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/']

    # Skip authentication for the excluded paths
    if not auth.require_auth(request.path, excluded_paths):
        return  # No authentication required for this path

    # Check if the request contains an Authorization header
    if auth.authorization_header(request) is None:
        abort(401)  # Unauthorized

    # Check if the current user can be identified (currently always None)
    if auth.current_user(request) is None:
        abort(403)  # Forbidden


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5001")
    app.run(host=host, port=port)
