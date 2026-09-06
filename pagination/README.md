# Pagination

This project implements three pagination approaches for a CSV dataset:
simple page-based pagination, pagination with hypermedia metadata, and
deletion-resilient index-based pagination.

## Files

- `0-simple_helper_function.py`: calculates page index ranges.
- `1-simple_pagination.py`: returns a requested dataset page.
- `2-hypermedia_pagination.py`: adds page navigation metadata.
- `3-hypermedia_del_pagination.py`: preserves pagination across deletions.

All modules target Python 3.9 and follow `pycodestyle` 2.5 conventions.
