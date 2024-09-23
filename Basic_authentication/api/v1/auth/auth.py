#!/usr/bin/env python3
"""
Auth module for API authentication.
This module defines the Auth class, which is responsible for
managing the authentication for the API.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class to manage the API authentication.
    
    This class contains methods that define the basic logic for 
    determining whether a path requires authentication, retrieving
    the authorization header, and fetching the current user.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if a given path requires authentication.

        Args:
            path (str): The request path to be checked.
            excluded_paths (List[str]): A list of paths that don't require authentication.

        Returns:
            bool: True if the path requires authentication, False otherwise.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normalize the path by adding a trailing slash if not present
        if not path.endswith('/'):
            path += '/'

        # Return False if the path is in the list of excluded paths
        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            str: The value of the Authorization header, or None if it is not present.
        """
        if request is None:
            return None

        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None

        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on the request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            User: The current user, or None if no user is authenticated.
        """
        return None
 