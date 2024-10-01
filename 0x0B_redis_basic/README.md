# Redis Cache with Python

This project demonstrates a simple `Cache` class that uses Redis to store data. The `Cache` class provides functionality to store data of different types (string, bytes, integer, float) in Redis with randomly generated keys.

## Project Structure

atlas-web_back_end/ │ ├── 0x0B_redis_basic/ │ ├── exercise.py # Contains the Cache class │ └── main.py # Main file to test the class

swift
Copy code

### `Cache` Class

- **Constructor (`__init__`)**: Initializes a Redis client and flushes the database (`flushdb`) to ensure it's empty.
- **`store` method**: 
  - Accepts `data` (of types: `str`, `bytes`, `int`, or `float`).
  - Generates a random key using `uuid`.
  - Stores the data in Redis using the generated key.
  - Returns the key.

## Prerequisites

- Python 3.x
- Redis installed locally
- `redis` Python package installed

### Installing Redis on macOS

If you're using macOS, install Redis via Homebrew:

```bash
brew install redis
To start Redis:


brew services start redis
Python Dependencies
Install the required redis package using pip3:


pip3 install redis
How to Run
Clone the repository:


git clone https://github.com/your-username/atlas-web_back_end.git
cd atlas-web_back_end/0x0B_redis_basic
Run the example:

The main file demonstrates how the Cache class works.


python3 main.py
Expected Output:

The script will generate a random key and store data in Redis. You should see output similar to:


3a3e8231-b2f6-450d-8b0e-0f38f16e8ca2
b'hello'
The first line is the randomly generated key, and the second is the stored value retrieved from Redis.

Example Usage
Here is an example of using the Cache class:

python
Copy code
from exercise import Cache

# Create a Cache instance
cache = Cache()

# Store some data
key = cache.store(b"hello")

# Retrieve the stored data
local_redis = redis.Redis()
print(local_redis.get(key))  # Should print: b'hello'
License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown
Copy code

---

### Key Sections:

1. **Project Overview**: Describes what the project does and includes the directory structure.
2. **Prerequisites**: Lists necessary tools and packages.
3. **Installation**: Explains how to install Redis and the required Python dependencies.
4. **Usage**: Details the usage of the `Cache` class with an example.
5. **License**: Placeholder for the license information.

You can modify the `git clone` URL and add more details to fit your specific needs