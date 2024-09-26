#!/usr/bin/env python3
"""
This module contains unit tests for utility functions in the `utils` module.

The tests cover the following functionalities:
- Accessing values in nested maps.
- Fetching JSON data from URLs using the `requests` library.
- Testing the `memoize` decorator to ensure proper caching.
"""

from parameterized import parameterized
import unittest
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the `access_nested_map` function.

    This function retrieves values from a nested dictionary by following
    a specified path (sequence of keys).
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the expected result."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised when the path is not present."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Unit tests for the `get_json` function.

    The `get_json` function fetches and returns JSON data from a given URL.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns the expected result from a URL."""
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Unit tests for the `memoize` decorator.

    The `memoize` decorator caches the result of a method so that subsequent
    calls return the cached value instead of recalculating it.
    """

    def test_memoize(self):
        """Test that the memoize decorator caches the result of a method."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
            TestClass, 'a_method', return_value=42
        ) as mock_method:
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            mock_method.assert_called_once()
