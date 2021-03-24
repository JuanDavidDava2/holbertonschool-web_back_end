#!/usr/bin/env python3
""" Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int):
    """ Write a function named index_range that takes
        two integer arguments page and page_size.
    """
    size = page * page_size
    return (size - page_size, size)
