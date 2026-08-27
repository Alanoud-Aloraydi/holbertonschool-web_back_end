#!/usr/bin/env python3
"""Measure the average runtime of concurrent random delays."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Run wait_n and return its total elapsed time divided by n."""
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.time() - start_time
    return total_time / n
