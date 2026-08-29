#!/usr/bin/env python3
"""Collect values from an asynchronous generator."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return ten values collected with an asynchronous comprehension."""
    return [value async for value in async_generator()]
