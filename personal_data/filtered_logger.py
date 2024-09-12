#!/usr/bin/env python3
"""
Module for logging user data processing with PII redaction.
"""

from typing import List
import logging
import re
from logging import StreamHandler, getLogger, INFO, NOTSET


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """
    Filters sensitive fields in a log message.

    Args:
        fields (list): A list of fields to be obfuscated.
        redaction (str): The string that will replace the field's value.
        message (str): The log message to be filtered.
        separator (str): The delimiter used in the message to separate fields.

    Returns:
        str: The filtered log message with the sensitive fields redacted.
    """
    return re.sub(f"({'|'.join(fields)})=[^{separator}]*",
                  lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    SEPARATOR = ";"

    def __init__(self,
                 fields: List[str]):
        """
        Initialize the formatter with a list of fields to redact.

        Args:
            fields (list): A list of fields to be obfuscated.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record by redacting sensitive information.
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


# Define PII fields (choose the most sensitive 5)
# Prioritize privacy for emails, SSNs, and passwords
PII_FIELDS = ("email", "ssn", "password")


def get_logger():
    """
    Returns logger named "user_data" for logging user data processing.

    The logger is configured to:

    - Log only up to INFO level.
    - Not propagate messages to other loggers.
    - Use a StreamHandler to log to the standard output (console).
    - Use a RedactingFormatter to redact PII fields.
    """

    logger = getLogger("user_data")
    logger.setLevel(INFO)  # Only log messages up to INFO level
    logger.propagate = False  # Do not propagate messages to other loggers

    handler = StreamHandler()  # Log to standard output (console)
    # Use RedactingFormatter with PII fields
    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
