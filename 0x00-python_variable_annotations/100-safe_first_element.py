#!/usr/bin/env python3
"""
Duck typing the first element of a sequence
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Parameters
    ----------
    lst (Sequence[Any]): a sequence type and it's a list of any type

    Return
    ------
    Union[Any, None]: The return va;ue could be of multiple types
    """
    if lst:
        return lst[0]
    else:
        return None
