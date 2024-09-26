#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json', return_value={"login": "test_org"})
    def test_org(self, org_name, expected_response, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.

        Args:
            org_name (str): Organization name to test.
            expected_response (dict): Expected result from the API.
            mock_get_json (Mock): Mocked get_json function.
        """
        # Initialize the client with the organization name
        client = GithubOrgClient(org_name)

        # Call the org method and capture the result
        result = client.org

        # Assert get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

        # Assert the result is as expected
        self.assertEqual(result, expected_response)