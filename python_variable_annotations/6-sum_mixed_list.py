#!/usr/bin/env python3
"""Provide a function for summing integers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of the integer and floating-point values in mxd_lst."""
    return float(sum(mxd_lst))
