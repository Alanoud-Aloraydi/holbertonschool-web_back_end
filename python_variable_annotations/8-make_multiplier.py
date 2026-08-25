#!/usr/bin/env python3
"""Provide a factory for floating-point multiplier functions."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiply(value: float) -> float:
        """Return value multiplied by the enclosing multiplier."""
        return value * multiplier

    return multiply
