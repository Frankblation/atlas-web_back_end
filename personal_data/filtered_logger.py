#!/usr/bin/env python3
"""Replacing their values with the redaction string."""

from typing import List
import logging
import re
from logging import StreamHandler, getLogger, INFO, NOTSET
from .RedactingFormatter import RedactingFormatter 

def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """
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
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with a list of fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record by redacting sensitive information.
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)

"""
Module for logging user data processing with PII redaction.
"""

# Define PII fields (choose the most sensitive 5)
PII_FIELDS = ("email", "ssn", "password")  # Prioritize privacy for emails, SSNs, and passwords


def get_logger():
  """
  Returns a pre-configured logger named "user_data" for logging user data processing.

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
  formatter = RedactingFormatter(fields=PII_FIELDS)  # Use RedactingFormatter with PII fields
  handler.setFormatter(formatter)

  logger.addHandler(handler)
  return logger

# Example usage (assuming this code is in a separate module)
user_data_logger = get_logger()
user_data_logger.info("Processing user data...")  # This will be logged
user_data_logger.debug("Detailed processing step...")  # This won't be logged (below INFO level)