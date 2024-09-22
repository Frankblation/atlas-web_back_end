#!/usr/bin/env python3
"""Auth module for API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to check if a path requires authentication.
        For now, it always returns False.

        Args:
            path (str): The request path.
            excluded_paths (List[str]): List of paths that don't require authentication.

        Returns:
            bool: False indicating no authentication is required.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Method to fetch the Authorization header from the request.
        For now, it always returns None.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            str: None indicating no Authorization header is available.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to get the current user.
        For now, it always returns None.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            User: None, representing no user is authenticated.
        """
        return None