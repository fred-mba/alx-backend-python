#!/usr/bin/env python3
"""
A type checking module using mypy
"""
from typing import Tuple, List, Any, Sequence, Union


def zoom_array(
    lst: Union[Tuple[Any, ...], Sequence[Any]],
    factor: int = 2
) -> List[Any]:
    """
    Parameters
    ----------
    lst (Union[Tuple[Any, ...], Sequence[Any]]): A union of a tuple or sequence
    of elements to zoom in.
    factor (int): standard factor for zoom

    Return
    ------
    List[Any]: A list with each repeated in `standard factor` times.
    """
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
