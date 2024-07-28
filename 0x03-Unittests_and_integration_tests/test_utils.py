#!/usr/bin/env python3
"""
Parameterized unittest module
"""
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """
        Parameters
        ----------
        nested_map: the input dictionary
        path: the tuple of keys to transverse
        expected: the expected result
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
