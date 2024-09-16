#!/usr/bin/env python3
"""salted the password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password with a salt using bcrypt.

    :param password: The password to be hashed.
    :return: The hashed password as a byte string.
    """
    # Convert the password to bytes if it's not already
    password_bytes = password.encode('utf-8')

    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password
