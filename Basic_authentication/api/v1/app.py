#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from api.v1.auth.auth import Auth
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize `auth` based on AUTH_TYPE environment variable
auth = None

# Check environment variable and configure authentication
# based on auth_type
auth_type = getenv("AUTH_TYPE")

if auth_type == "auth":
    auth = Auth()  # Create an instance of Auth


@app.before_request
def before_request_func():
    """Before each request, apply authentication logic."""
    # Do nothing if `auth` is None
    if auth is None:
        return

    # Excluded paths that don't require authentication
    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/']
    
    # Normalize the request path by adding a trailing slash if not present
    path = request.path
    if not path.endswith('/'):
        path += '/'

    if request.path in excluded_paths:
        return

    if request.path not in excluded_paths and \
            auth.require_auth(request.path, excluded_paths):
        if auth.authorization_header(request) is None:
            abort(401)  # Unauthorized
    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Not authorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
