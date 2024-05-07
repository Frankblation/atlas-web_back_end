#!/usr/bin/env python3
"""
Async comprehension that collects 10 random numbers using async generator.
"""

import asyncio
from typing import List
from random import uniform
import importlib

async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension over async_generator.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [i async for i in async_generator()]

async def main():
    print(await async_comprehension())

asyncio.run(main())
