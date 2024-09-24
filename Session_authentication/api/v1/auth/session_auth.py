#!/usr/bin/env python3
"""
SessionAuth module for handling session-based authentication.
"""
import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """
    SessionAuth class that inherits from Auth.
    Manages session IDs and user sessions.
    """

    # Class attribute: Dictionary to store session IDs and corresponding user
    # IDs
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a given user_id.

        Args:
            user_id (str): The user ID for which the session is created.

        Returns:
            str: The created session ID or None if user_id is invalid.
        """
        # Return None if user_id is None or not a string
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a new session ID using uuid4
        session_id = str(uuid.uuid4())

        # Store the session ID and user ID in the dictionary
        self.user_id_by_session_id[session_id] = user_id

        # Return the generated session ID
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieves the user ID based on a session ID.

        Args:
            session_id (str): The session ID to retrieve the user ID.

        Returns:
            str: The user ID associated with the session ID, or None, invalid.
        """
        # Return None if session_id is None or not a string
        if session_id is None or not isinstance(session_id, str):
            return None

        # Use the dictionary's get() method to retrieve the user ID
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Return the User instance based on the session cookie (_my_session_id).
        """
        # Get the session ID from the request cookies
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        # Get the user ID based on the session ID
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        # Retrieve the user instance from the database
        user = User.get(user_id)
        return user
