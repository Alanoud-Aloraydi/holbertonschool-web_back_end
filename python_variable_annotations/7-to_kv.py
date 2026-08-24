#!/usr/bin/env python3
"""Provide a function that pairs a key with a squared value."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing k and the square of v."""
    return (k, v ** 2)
