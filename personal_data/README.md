PII Handling, Logging, Encryption, and Authentication

Project Overview

This project focuses on handling Personally Identifiable Information (PII) securely. It includes implementing a log filter to obfuscate PII fields, encrypting passwords, validating passwords, and authenticating to a database using environment variables.

Resources

To complete this project, you may want to review the following resources:

What Is PII, non-PII, and Personal Data?
Python Logging Documentation
bcrypt Package
Logging to Files, Setting Levels, and Formatting
Learning Objectives

By the end of this project, you should be able to:

Identify examples of Personally Identifiable Information (PII).
Implement a log filter that obfuscates PII fields.
Encrypt a password and verify the validity of an input password.
Authenticate to a database using environment variables.
Requirements

Python Version: 3.9
Operating System: Ubuntu 20.04 LTS
Code Style: All code follows the pycodestyle (version 2.5) style guide.
File Naming: All Python files should end with a newline and start with #!/usr/bin/env python3.
Documentation: Each module, class, and function is documented with detailed explanations of their purpose and usage. All functions and methods are type-annotated.
Executable Files: All your Python files must be executable.
File Length: The length of your files will be verified using the wc command.
Setup Instructions

Clone the Repository:
bash
Copy code
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install Dependencies: If there are any dependencies, create a virtual environment and install them:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Features and Usage

1. Handling Personally Identifiable Information (PII)
Examples of PII:

Full name
Social Security Number (SSN)
Email address
Phone number
Credit card information
2. Log Filter for Obfuscating PII
The log filter is designed to obfuscate PII fields in logs to ensure sensitive information is not exposed.

Example Usage:

python
Copy code
import logging
from your_module import PIIObfuscationFilter

logger = logging.getLogger("your_logger")
logger.addFilter(PIIObfuscationFilter())

logger.info("User info: name=John Doe, email=johndoe@example.com")
3. Password Encryption and Validation
This project uses the bcrypt package to securely encrypt passwords and validate user input against stored hashed passwords.

Example Usage:

python
Copy code
from your_module import encrypt_password, validate_password

hashed_password = encrypt_password("my_secure_password")
is_valid = validate_password("my_secure_password", hashed_password)
print(is_valid)  # Should print True
4. Database Authentication Using Environment Variables
To securely authenticate to a database, the project uses environment variables to store sensitive credentials.

Example:

bash
Copy code
export DB_USER="your_db_user"
export DB_PASSWORD="your_db_password"
export DB_HOST="localhost"
export DB_NAME="your_db_name"
In your Python code:

python
Copy code
import os
import mysql.connector

db_connection = mysql.connector.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME")
)
Testing

To ensure everything works as expected, you can run the test suite:

bash
Copy code
python3 -m unittest discover tests/
License