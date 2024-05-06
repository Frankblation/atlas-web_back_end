#!/usr/bin/env python3
'''
This script measures the total execution
time for the wait_n coroutine.
'''
import asyncio
from time import perf_counter
from typing import List
from random import uniform
from asyncio import run


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


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with
    the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*tasks))


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for the wait_n coroutine.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average time taken for each coroutine execution.
    """
    start_time = perf_counter()
    run(wait_n(n, max_delay))
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n
