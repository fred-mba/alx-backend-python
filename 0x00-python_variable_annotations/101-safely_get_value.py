#!/usr/bin/env python3
"""
More on duck-type annotations
"""
from typing import TypeVar, Mapping, Optional, Any, Union


T = TypeVar('T')
U = Union[T, None]
V = Union[Any, None]


def safely_get_value(dct: Mapping, key: Any, default: U = None) -> V:
    """
    Parameters
    ----------
    dct (Mapping[str, T]): A dictionary with string keys and values of type `T`
    key (str): dictionary's keys
    default U = None: default is an optional value of type T.
    U allows it to be None or any value of type T.

    Return
    ------
    V: Function can return value of any type or None.
    """
    if key in dct:
        return dct[key]
    else:
        return default
