#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient."""

    @parameterized.expand([
        ("google", {"login": "google", "repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"login": "abc", "repos_url": "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch('utils.get_json')  # Patch the get_json function
    def test_org(self, org_name, expected_response, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.

        Args:
            org_name (str): Organization name to test.
            expected_response (dict): Expected result from the API.
            mock_get_json (Mock): Mocked get_json function.
        """
        # Set the return value for the mock
        mock_get_json.return_value = expected_response

        # Initialize the client with the organization name
        client = GithubOrgClient(org_name)

        # Call the org property to trigger the get_json call
        result = client.org

        # Assert get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(client.ORG_URL.format(org=org_name))

        # Assert the result is as expected
        self.assertEqual(result, expected_response)