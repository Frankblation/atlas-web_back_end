#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):

    @patch('utils.get_json')
    def test_org(self, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value for 'google'."""
        mock_get_json.return_value = {
            'login': 'google', 
            'repos_url': 'https://api.github.com/orgs/google/repos'
        }
        client = GithubOrgClient('google')
        org_data = client.org()
        self.assertEqual(org_data['login'], 'google')
        self.assertEqual(org_data['repos_url'], 'https://api.github.com/orgs/google/repos')
        mock_get_json.assert_called_once_with(client.ORG_URL.format(org='google'))

    @parameterized.expand([
        ('google', {'login': 'google', 'repos_url': 'https://api.github.com/orgs/google/repos'}),
        ('abc', {'login': 'abc', 'repos_url': 'https://api.github.com/orgs/abc/repos'}),
    ])
    @patch('utils.get_json')
    def test_org_parametrized(self, org_name, expected_data, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value for various organizations."""
        mock_get_json.return_value = expected_data
        client = GithubOrgClient(org_name)
        org_data = client.org()
        self.assertEqual(org_data['login'], expected_data['login'])
        self.assertEqual(org_data['repos_url'], expected_data['repos_url'])
        mock_get_json.assert_called_once_with(client.ORG_URL.format(org=org_name))

if __name__ == "__main__":
    unittest.main()
