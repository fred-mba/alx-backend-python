#!/usr/bin/env python3
"""
Module implementation of complex types-list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Type-annotated function which takes a list input_list of floats as argument
    and returns list of floats.

    Parameters
    ----------
    input_list (List[float]): A list of floating point numbers to sum up.

    Returns
    -------
    float: The sum of the number in the list
    """
    return sum(input_list)
