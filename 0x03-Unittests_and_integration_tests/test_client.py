#!/usr/bin/env python3
"""
Parameterize and patch as decorators module
"""
import unittest
from unittest.mock import Mock, MagicMock, patch, PropertyMock
from parameterized import parameterized, parameterized_class
from typing import Any, Dict
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrg class to test the GithubOrgClient
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(
             self,
             org_name: str,
             expected: Dict[str, Any],
             mock_get_json: MagicMock) -> None:
        """
        Takes an org_name as a str, the expected Dict result, and
        mocked_get_json method and returns nothing.
        """
        mock_get_json.return_value = expected

        org_client = GithubOrgClient(org_name)

        self.assertEqual(org_client.org, expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self) -> None:
        """
        Unit-test GithubOrgclient._public_repos_url.
        """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos"
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """
        Unit-test GithubOrgClient.public_repos
        """
        test_payload = {
            'repos': [
                {
                    "id": 1936771,
                    "name": "truth",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/truth",
                    "created_at": "2011-06-22T18:55:12Z",
                    "updated_at": "2024-07-29T19:13:42",
                    "language": "Java",
                    "has_issues": True,
                    "watchers": 2712,
                    "default_branch": "master",
                },
                {
                    "id": 3975462,
                    "name": "anvil-build",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/anvil-build",
                    "created_at": "2012-04-09T20:09:24Z",
                    "updated_at": "2023-12-22T11:30:23Z",
                    "language": "Python",
                    "has_issues": True,
                    "watchers": 56,
                    "default_branch": "master",
                },
            ]
        }

        mock_get_json.return_value = test_payload["repos"]

        public_repos_url = "https://api.github.com/orgs/google/repos"
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "public_repos_url"

            self.assertEqual(
               GithubOrgClient("google").public_repos(),
               ["truth", "anvil-build"])

            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(
            self, repo: Dict[Any, str],
            license_key: str, expected: bool) -> None:
        """
        Function to unit-test GithubOrgClient.has_license
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
