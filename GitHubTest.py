import unittest
from unittest.mock import patch
import GitHubApi


class TestGitHub(unittest.TestCase):
    @patch("GitHubApi.get_repo")
    def test_get_repo_with_invalid_user(self, mock_get_repo):
        mock_get_repo.return_value = False
        self.assertFalse(GitHubApi.get_repo('blkfjayhatw'))

    @patch("GitHubApi.get_repo")
    def test_get_repo_with_valid_user(self, mock_get_repo):
        mock_get_repo.return_value = True
        self.assertTrue(GitHubApi.get_repo('ArunRao1997'))

    @patch("GitHubApi.get_repo")
    def test_get_repo_with_user_with_no_repos(self, mock_get_repo):
        mock_get_repo.return_value = False
        self.assertFalse(GitHubApi.get_repo('GautamP2393'))

    @patch("GitHubApi.get_repo")
    def test_get_repo_returns_boolean(self, mock_get_repo):
        mock_get_repo.return_value = True
        self.assertIsInstance(GitHubApi.get_repo('richkempinski'), bool)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
