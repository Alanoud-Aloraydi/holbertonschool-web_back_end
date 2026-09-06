#!/usr/bin/env python3
"""Paginate a CSV dataset using page and page-size parameters."""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end indexes for a one-indexed page."""
    start_index = (page - 1) * page_size
    return start_index, start_index + page_size


class Server:
    """Paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with an empty dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load the dataset once and return its rows without the header."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1,
                 page_size: int = 10) -> List[List]:
        """Return the requested page of data or an empty out-of-range page."""
        assert (
            isinstance(page, int)
            and not isinstance(page, bool)
            and page > 0
        )
        assert (
            isinstance(page_size, int)
            and not isinstance(page_size, bool)
            and page_size > 0
        )

        start_index, end_index = index_range(page, page_size)

        if start_index >= len(self.dataset()):
            return []
        return self.dataset()[start_index:end_index]
