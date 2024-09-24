#!/usr/bin/env python3
"""
Session authentication view for handling login.
"""

from flask import request, jsonify, abort
from models.user import User
from os import getenv
from api.v1.views import app_views  # Import app_views for routing
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    POST /api/v1/auth_session/login: Login a user via session authentication.

    Retrieves the user's email and password from the request, verifies them,
    creates a session for the user if valid, and returns the user data along
    with setting the session cookie.

    Returns:
        - 400 if the email or password is missing.
        - 404 if the email is not found.
        - 401 if the password is incorrect.
        - 200 with the user information and session cookie if successful.
    """
    # Get email and password from the form
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if email is missing
    if not email:
        return jsonify({"error": "email missing"}), 400

    # Check if password is missing
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Retrieve the user by email
    try:
        users = User.search({"email": email})
    except Exception:
        users = []

    # Check if no user found
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    # Get the first user (assuming emails are unique)
    user = users[0]

    # Check if password is valid
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Import auth dynamically to avoid circular import
    from api.v1.app import auth

    # Create session for the user
    session_id = auth.create_session(user.id)

    # Return the user information with session cookie
    session_name = getenv("SESSION_NAME", "_my_session_id")
    response = jsonify(user.to_json())
    response.set_cookie(session_name, session_id)

    return response


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """
    Handle user logout by destroying the session.
    """
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
