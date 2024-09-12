#!/usr/bin/env python3
"""replacing their values with the redaction string."""

from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
        Args:
        fields (list): A list of fields to be obfuscated.
        redaction (str): The string that will replace the field's value.
        message (str): The log message to be filtered.
        separator (str): The delimiter used in the message to separate fields.

    Returns:
        str: The filtered log message with the sensitive fields redacted.
    """
    return re.sub(f"({'|'.join(fields)})=[^{separator}]*", lambda m: f"{m.group(1)}={redaction}", message)
