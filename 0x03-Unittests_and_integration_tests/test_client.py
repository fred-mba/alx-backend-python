#!/usr/bin/env python3
"""
Parameterize and patch as decorators module
"""
import unittest
from unittest.mock import Mock, MagicMock, patch
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
