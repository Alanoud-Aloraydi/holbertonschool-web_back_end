#!/usr/bin/env python3
"""Provide a function that safely reads the first sequence element."""

from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first item in lst, or None when lst is empty."""
    if lst:
        return lst[0]
    return None
