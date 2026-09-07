#!/usr/bin/env python3
"""Provide deletion-resilient index-based hypermedia pagination."""

import csv
import math
from typing import Dict, List


class Server:
    """Paginate a database of popular baby names despite deleted rows."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with empty dataset caches."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load the dataset once and return its rows without the header."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return dataset rows indexed by their original positions."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                index: row for index, row in enumerate(dataset)
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """Return a page while preserving original indexes after deletions."""
        assert index is None or (
            isinstance(index, int) and not isinstance(index, bool)
            and 0 <= index < len(self.dataset())
        )

        if index is None:
            index = 0

        indexed_data = self.indexed_dataset()
        data = []
        next_index = index

        while (
            len(data) < page_size
            and next_index < len(self.dataset())
        ):
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
