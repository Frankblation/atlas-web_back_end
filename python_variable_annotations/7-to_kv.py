#!/usr/bin/env python3
"""
This script defines a function that converts 
a key-value pair into a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element 
    is the string k and the second element
    is the square of the int/float v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple containing the 
        string k and the square of v as a float.
    """
    return (k, float(v) ** 2)
