#!/usr/bin/env python3
"""
A module implementation of complex types-mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float | int]]) -> float:
    """
    Parameters
    ----------
    mx_list (List[float, int]): A list of mixed int, and float numbers

    Returns
    -------
    float: The sum of the mixed numbers as float type
    """
    return sum(mxd_lst)
