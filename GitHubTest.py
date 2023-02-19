import unittest

from GitHubApi import get_repo


class TestGitHub(unittest.TestCase):
    def test_get_repo_with_invalid_user(self):
        self.assertFalse(get_repo('blkfjayhatw'))

    def test_get_repo_with_valid_user(self):
        self.assertTrue(get_repo('ArunRao1997'))

    def test_get_repo_with_user_with_no_repos(self):
        self.assertFalse(get_repo('GautamP2393'))

    def test_get_repo_returns_boolean(self):
        self.assertIsInstance(get_repo('richkempinski'), bool)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
