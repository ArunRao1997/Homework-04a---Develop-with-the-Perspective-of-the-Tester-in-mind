import unittest
from GitHubApi import get_repo


class TestGitHub(unittest.TestCase):
    def test_get_repo_with_invalid_user(self):
        self.assertFalse(get_repo('aljhdfjabfbfb'))

    def test_get_repo_with_valid_user(self):
        self.assertTrue(get_repo('vaibhavvashisht16'))

    def test_get_repo_with_user_with_no_repos(self):
        self.assertFalse(get_repo('GautamP2393'))

    def test_get_repo_returns_boolean(self):
        self.assertIsInstance(get_repo('vaibhavvashisht16'), bool)


if __name__ == 'main':
    unittest.main()
