#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from api.v1.auth.auth import Auth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize `auth` based on AUTH_TYPE environment variable
auth = None
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


To implement the request validation for securing the API, we need to follow a few steps. Here's a breakdown of how to update your authentication logic and integrate it into the Flask application:

1. Update authorization_header method in api/v1/auth/auth.py
The authorization_header method needs to return the Authorization header from the request or None if the request object is None or the header is missing.

2. Modify app.py to load Auth based on the AUTH_TYPE environment variable
You will create an auth variable and assign an instance of Auth if the AUTH_TYPE environment variable is set to auth.

3. Add a before_request function in app.py
This function will intercept all incoming requests and:

Skip authentication for specific paths (/status, /unauthorized, /forbidden).
If auth.authorization_header(request) returns None, respond with a 401 Unauthorized error.
If auth.current_user(request) returns None, respond with a 403 Forbidden error.
Step 1: Update authorization_header in api/v1/auth/auth.py
Here’s the implementation of the authorization_header method in api/v1/auth/auth.py:

python
Copy code
#!/usr/bin/env python3
"""
Auth module for API authentication.
"""
from flask import request


class Auth:
    """Auth class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: list) -> bool:
        """
        Check if the given path requires authentication.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normalize path: Add a trailing slash if not present
        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header from the request, or None.
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None):
        """
        Returns the current user based on the request (to be implemented).
        """
        return None
authorization_header: Returns the Authorization header from the request if present, otherwise None.
Step 2: Update app.py to load auth based on AUTH_TYPE
Here’s the app.py file where you load the auth instance and handle the request filtering:

python
Copy code
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

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)