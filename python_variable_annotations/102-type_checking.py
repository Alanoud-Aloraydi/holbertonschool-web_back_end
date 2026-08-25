#!/usr/bin/env python3
"""Demonstrate a list-producing function validated with mypy."""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a list with each tuple item repeated factor times."""
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
