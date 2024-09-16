#!/usr/bin/env python3
"""Replacing their values with the redaction string."""

from typing import List
import logging
import re
import os
import mysql.connector
from mysql.connector import connect

# Define PII_FIELDS with sensitive fields
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """
    Obfuscates fields in a message.

    Args:
        fields (list): A list of fields to be obfuscated.
        redaction (str): The string that will replace the field's value.
        message (str): The log message to be filtered.
        separator (str): The delimiter used in the message to separate fields.

    Returns:
        str: The filtered log message with the sensitive fields redacted.
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class to hide PII """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with a list of fields to redact.

        Args:
            fields (List[str]): Fields to be redacted from the logs.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record by redacting sensitive information.

        Args:
            record (logging.LogRecord): Log record object to be formatted.

        Returns:
            str: Formatted log message with sensitive data redacted.
        """
        original_message = super().format(record)
        return filter_datum(
            self.fields,
            self.REDACTION,
            original_message,
            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Create a logger object with redacting capabilities.

    Returns:
        logging.Logger: instance stream handler and RedactingFormatter.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create a stream handler with the RedactingFormatter
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


def get_db():
    """
    Returns a MySQLConnection object to the specified database.

    Uses environment variables for credentials.

    Returns:
        mysql.connector.connection.MySQLConnection: A connection object.
    """
    username = os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.environ.get('PERSONAL_DATA_DB_NAME')

    if not database:
        raise ValueError(
            "PERSONAL_DATA_DB_NAME environment variable is required.")

    connection = connect(
        user=username,
        password=password,
        host=host,
        database=database
    )

    return connection


def main() -> None:
    """
    Main function to retrieve data from the users table and log it
    with sensitive fields redacted.
    """
    logger = get_logger()
    db_connection = get_db()
    cursor = db_connection.cursor()

    # Query the users table to retrieve all rows
    cursor.execute("SELECT * FROM users;")

    # Retrieve the column names (to match against PII_FIELDS)
    columns = [desc[0] for desc in cursor.description]

    # Log each user entry, applying redaction
    for row in cursor.fetchall():
        # Create a formatted string for logging
        message = "; ".join(
            f"{col}={val}" for col, val in zip(
                columns, row)) + ";"
        logger.info(message)

    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
