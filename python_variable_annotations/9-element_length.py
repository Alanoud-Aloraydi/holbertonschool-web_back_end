#!/usr/bin/env python3
"""Provide a function that pairs sequence elements with their lengths."""

from typing import Iterable, List, Sequence, Tuple


def element_length(
        lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return each sequence in lst paired with its length."""
    return [(item, len(item)) for item in lst]
