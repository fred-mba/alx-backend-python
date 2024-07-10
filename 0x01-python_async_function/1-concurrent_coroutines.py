#!/usr/bin/python3
"""
The module runs multiple `wait_random` coroutines concurrently and gather their
results in a list.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a sorted list of all delays.

    Parameters
    ----------
    n (int): number of times to iterate while appending the result
    ma_delay (int): upper limit for the random delay time.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    sorted_delays = sorted(delays)

    return sorted_delays
