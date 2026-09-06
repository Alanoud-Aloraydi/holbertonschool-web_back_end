#!/usr/bin/env python3
"""Provide a helper for calculating pagination index ranges."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end indexes for a one-indexed page."""
    start_index = (page - 1) * page_size
    return start_index, start_index + page_size
