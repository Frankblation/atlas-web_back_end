#!/usr/bin/env python3
"""Async generator"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10
    after waiting for 1 second, repeated 10 times.

    Yields:
        float: Random number between 0 and 10.

    Returns:
        AsyncGenerator[float, NoneType]: Asynchronous generator.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def print_yielded_values() -> None:
    """
    Consume the generated values from async_generator and print them.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
