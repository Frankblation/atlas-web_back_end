#!/usr/bin/env python3
"""
This script defines a regular function that returns an asyncio.Task.
"""

import asyncio
from typing import Any
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a
    random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The random delay waited.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> Any:
    """
    Regular function that returns an asyncio.Task.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        Task: An asyncio.Task representing the
         execution of the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
