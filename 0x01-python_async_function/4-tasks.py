#!/usr/bin/env python3
"""
This module use `task_wait_n` similar to `wait_n` but utilizing
`task_wait_random` to create and manage asynchronous tasks.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a sorted list of all delays.

    Parameters
    ----------
    n (int): number of times to iterate while appending the result
    ma_delay (int): upper limit for the random delay time.
    """
    delays = await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n)))

    sorted_delays = sorted(delays)

    return sorted_delays
