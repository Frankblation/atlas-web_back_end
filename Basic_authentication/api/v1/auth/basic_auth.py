#!/usr/bin/env python3
"""
BasicAuth module for API authentication.
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth.
    For now, this class is empty but will be extended later.
    """
    pass


def extract_base64_authorization_header(
        self, authorization_header: str) -> str:
    """ Function that extracts the base 64 part of the header

        Args:
            - self
            - authorization_header: Header to be parsed

        Return:
            - The base 64 part of the header
    """
    # No header is provided
    if authorization_header is None:
        return None

    # Header must be a valid string
    if not isinstance(authorization_header, str):
        return None

    header = "Basic "

    # Header must start with Basic
    if authorization_header.startswith(header):

        # Calculate the position at the end of header
        start_index = len(header)
        return authorization_header[start_index:]
    else:
        return None

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """ Function that extracts the base 64 part of the header

            Args:
                - self
                - authorization_header: Header to be parsed

            Return:
                - The base 64 part of the header
        """
    # No header is provided
    if authorization_header is None:
        return None

    # Header must be a valid string
    if not isinstance(authorization_header, str):
        return None

    header = "Basic "

    # Header must start with Basic
    if authorization_header.startswith(header):

        # Calculate the position at the end of header
        start_index = len(header)
        return authorization_header[start_index:]
    else:
        return None
