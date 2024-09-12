#!/usr/bin/env python3
"""replacing their values with the redaction string."""


import re


def filter_datum(fields, redaction, message, separator):
    """
        Args:
        fields (list): A list of fields to be obfuscated.
        redaction (str): The string that will replace the field's value.
        message (str): The log message to be filtered.
        separator (str): The delimiter used in the message to separate fields.

    Returns:
        str: The filtered log message with the sensitive fields redacted.
    """
    for field in fields:
        pattern = f'{field}=.*?{separator}'
        message = re.sub(pattern, f'{field}={redaction}{separator}', message)

    return message
