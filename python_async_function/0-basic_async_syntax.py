#!/usr/bin/env python3
"""Provide a coroutine that waits for a random duration."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for and return a random delay between zero and max_delay."""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
