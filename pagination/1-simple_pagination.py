#!/usr/bin/env python3
"""This module provides a Server class to paginate a dataset of popular baby names.
It includes the following features:

1. `index_range(page, page_size)`: Returns a tuple of start and end indices for pagination.
2. `Server` class:
   - `dataset()`: Loads and caches the dataset from a CSV file, excluding the header.
   - `get_page(page, page_size)`: Returns a subset of the dataset corresponding to the given page and page size.

The data is loaded from a CSV file named 'Popular_Baby_Names.csv'. The dataset is cached to optimize repeated access.

Usage:
    Instantiate the Server class and use its methods to paginate through the dataset.
"""""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing the start and end index for pagination."""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset based on the page and page size"""
        # Validate input arguments
        assert isinstance(
            page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(
            page_size, int) and page_size > 0, "Page size must be a positive integer"

        # Get the dataset
        dataset = self.dataset()

        # Use index_range to get the start and end index
        start, end = index_range(page, page_size)

        # Return the appropriate page or an empty list if out of range
        return dataset[start:end] if start < len(dataset) else []
