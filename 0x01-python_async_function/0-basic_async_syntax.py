#!/usr/bin/env python3
"""
This module generates a random float between 0-10 and pauses
the routine for the genarated delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns the delay after the wait is complete

    Parameters
    ----------
    max_delay (int): default value set to 10
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
