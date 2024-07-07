#!/usr/bin/env python3
"""
A module snippet of a duck type iterable object
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns list of tuples where each tuple contains an element from the
    input list and its length.

    Parameters
    ----------
    lst (Iterable[Sequence]): Contains iterable sequence elements.

    Return
    ------
    List[Tuple[Sequence, int]]: List of tuples each containing elements with
    different sequence.
    """
    return [(i, len(i)) for i in lst]
