#!/usr/bin/env python3
"""
BasicAuth module for API authentication.
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth.
    This class provides methods to handle the Basic Authentication process.
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 part

        Args:
            authorization_header (str): The full Authorization header string.

        Returns:
            str: The Base64 encoded part of the header, or None
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        # The Authorization header
        # Base64 string
        if not authorization_header.startswith("Basic "):
            return None

        if not isinstance(authorization_header, str):
            return None

        # The Authorization header must start with 'Basic ' followed by the
        # Base64 string
        if not authorization_header.startswith("Basic "):
            return None

        # Return the part of the header after 'Basic '
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes the Base64

        Args:
            base64_authorization_header (str): The Base64 encoded part

        Returns:
            str: The decoded value as a UTF-8 string, or None
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            # Decode the Base64 string
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts the user email and password from the Base64 decoded.

        Args:
            decoded_base64_authorization_header (str): The decoded Base64 string

        Returns:
            (str, str): The user email and password, or (None, None) if invalid.
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        # Check if the string contains a colon to separate email and password
        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Split the string on the first occurrence of the colon
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password
