#!/usr/bin/env python3
"""Measure concurrent execution of asynchronous comprehensions."""

import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """Run four asynchronous comprehensions and return their total runtime."""
    start_time: float = time.perf_counter()
    await asyncio.gather(
        *(async_comprehension() for _ in range(4))
    )
    return time.perf_counter() - start_time
