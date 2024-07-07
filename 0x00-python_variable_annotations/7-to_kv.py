#!/usr/bin/env python3
"""
A module implemetation of complex types-string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of a string and a square of float

    Parameters
    ----------
    k (str): The string key.
    v (Union[int, float]): The number which can be an integer or a float.
    """
    return k, v ** 2
