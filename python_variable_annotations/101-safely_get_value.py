#!/usr/bin/env python3
"""Provide a typed helper for retrieving values from mappings."""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
        dct: Mapping, key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """Return the mapped value for key, or default when key is absent."""
    if key in dct:
        return dct[key]
    return default
