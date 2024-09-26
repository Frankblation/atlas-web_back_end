import unittest
from unittest.mock import patch
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):

    @patch('utils.get_json')
    def test_org(self, mock_get_json):
        mock_get_json.return_value = {'login': 'google', 'repos_url': 'https://api.github.com/orgs/google/repos'}
        client = GithubOrgClient('google')
        org_data = client.org()
        self.assertEqual(org_data['login'], 'google')
        self.assertEqual(org_data['repos_url'], 'https://api.github.com/orgs/google/repos')
        mock_get_json.assert_called_once_with(client.ORG_URL.format(org='google'))