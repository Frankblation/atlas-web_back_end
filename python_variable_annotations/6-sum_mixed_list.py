#!/usr/bin/env python3
"""sum mixed of eleements"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of elements in a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of elements in the input list.
    """
    return sum(mxd_lst)
