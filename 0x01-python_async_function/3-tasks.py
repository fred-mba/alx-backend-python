#!/usr/bin/env python3
"""
Creates an asyncio task from a regular function.
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an `asyncio.Task` by calling asyncio.create_task on
    `wait_random` coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
