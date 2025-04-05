from github import Github

def list_repos(username: str):
    g = Github()  # No token needed for public info
    user = g.get_user(username)
    return [repo.name for repo in user.get_repos()]
