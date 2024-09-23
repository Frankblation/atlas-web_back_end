#!/usr/bin/env python3
"""
SessionAuth module for handling session-based authentication.
"""
import uuid
from api.v1.auth.auth import Auth


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
