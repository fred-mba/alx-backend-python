#!/usr/bin/env python3
"""
Parameterized unittest module
"""
import unittest
from unittest.mock import patch, Mock
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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """
        Uses the assertRaises context manager to test that a KeyError is
        raised for the inputs.
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class to mock the HTTP calls
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})

    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """
        Creates a mock_reponse object with json() return value
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get', return_value=mock_response) as mock_req:
            self.assertEqual(get_json(test_url), test_payload)
            mock_req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Memoization test class
    """
    def test_memoize(self):
        """
        Test memoize method
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()

        with patch.object(
                TestClass,
                'a_method',
                return_value=42) as mock_a_method:

            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)

            mock_a_method.assert_called_once()
