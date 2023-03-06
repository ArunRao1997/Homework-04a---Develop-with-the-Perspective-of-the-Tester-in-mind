import unittest
from unittest.mock import patch
import GitHubApi


class TestGitHub(unittest.TestCase):
    @patch("GitHubApi.get_repo")
    def test_get_repo_with_valid_user(self, mock_get_repo):
        mock_get_repo.return_value = [200, {"Search_engine": "2",
                                            "kapilparsodkar/FitCzar-fitness-App": "14",
                                            "helloworld": "1",
                                            "SSW_567_HW_02a_Triangle": "8",
                                            "Homework-04a---Develop-with-the-Perspective-of-the-Tester-in-mind": "12",
                                            "SSW-567-HW-05-Static-Code-Analysis": "10",
                                            "JPMC_Virtual_Experience": "4"}]
        self.assertTrue(GitHubApi.get_repo("ArunRao1997")[0])

    @patch("GitHubApi.get_repo")
    def test_get_repo_return_value_with_valid_user(self, mock_get_repo):
        mock_get_repo.return_value = [200, {"Search_engine": "2",
                                            "kapilparsodkar/FitCzar-fitness-App": "14",
                                            "helloworld": "1",
                                            "SSW_567_HW_02a_Triangle": "8",
                                            "Homework-04a---Develop-with-the-Perspective-of-the-Tester-in-mind": "12",
                                            "SSW-567-HW-05-Static-Code-Analysis": "10",
                                            "JPMC_Virtual_Experience": "4"}]
        self.assertEqual(mock_get_repo()[1], GitHubApi.get_repo("ArunRao1997")[1])

    @patch("GitHubApi.get_repo")
    def test_get_repo_with_invalid_user(self, mock_get_repo):
        mock_get_repo.return_value = False
        self.assertFalse(GitHubApi.get_repo('blkfjayhatw'))

    @patch("GitHubApi.get_repo")
    def test_get_repo_return_value_with_invalid_user(self, mock_get_repo):
        mock_get_repo.return_value = False
        self.assertIs(mock_get_repo(), GitHubApi.get_repo('blkfjayhatw'))

    @patch("GitHubApi.get_repo")
    def test_get_repo_return_value_with_user_with_no_repos(self, mock_get_repo):
        mock_get_repo.return_value = [200, {""}]
        self.assertTrue(GitHubApi.get_repo("GautamP2393")[0])

    @patch("GitHubApi.get_repo")
    def test_get_repo_with_user_with_no_repos(self, mock_get_repo):
        mock_get_repo.return_value = [200, {""}]
        self.assertIs(mock_get_repo()[1], GitHubApi.get_repo("GautamP2393")[1])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
