#!/usr/bin/env python3
"""
Measure Runtime Module

This module contains a coroutine to measure the total runtime of executing
async_comprehension function four times in parallel.
"""

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing
    async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = perf_counter()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end_time = perf_counter()

    return end_time - start_time
