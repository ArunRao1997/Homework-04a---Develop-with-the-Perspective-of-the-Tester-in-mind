import requests


def get_repo(username):
    response = requests.get(f"https://api.github.com/users/{username}/repos")
    if response.status_code != 200:
        print("Invalid User")
        return False
    repos = response.json()
    if not repos:
        print("There are no repositories")
        return False
    for repo in repos:
        commits_url = repo['commits_url'].split("{")[0]
        response = requests.get(commits_url)
        commits = response.json()
        print(f"Repo: {repo['name']} Number Of Commits: {len(commits)}")
    return True


def get_username():
    username = input("Enter user ID from GitHub: ")
    get_repo(username)


get_username()
