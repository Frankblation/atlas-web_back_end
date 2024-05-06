#!/usr/bin/env python3
"""
The code is similar to wait_n
except task_wait_random is being called
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that waits for a random delay using task_wait_random.

    Args:
        n (int): The number of times to call task_wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    delay_list = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay_list
            for delay_list in asyncio.as_completed(delay_list)]
