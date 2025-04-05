from utils.github_helper import list_repos

if __name__ == "__main__":
    username = "octocat"  # replace with any username
    repos = list_repos(username)
    print(f"Repositories for {username}:")
    for repo in repos:
        print("-", repo)
