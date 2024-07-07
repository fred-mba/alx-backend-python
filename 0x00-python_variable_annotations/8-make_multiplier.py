#!/usr/bin/env python3
"""
Module implentation of a Callable type hint
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function product of a float and the multiplier.

    Parameters
    ----------
    multiplier (float): Multiplier to be used to multiply the float.
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func
