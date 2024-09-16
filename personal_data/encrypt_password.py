#!/usr/bin/env python3
"""salt and validify"""
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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate a password against a hashed password.

    :param hashed_password: The hashed password to check against.
    :param password: The password to validate.
    :return: True if the password matches the hashed password, otherwise False.
    """
    # Convert the password to bytes if it's not already
    password_bytes = password.encode('utf-8')

    # Check if the given password matches the hashed password
    return bcrypt.checkpw(password_bytes, hashed_password)
