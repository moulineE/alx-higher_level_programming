#!/usr/bin/python3
"""
a Python script that list 10 commits (from the most recent to oldest)
of the repository using the GitHub API
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    repo = sys.argv[1]
    u_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10"\
        .format(u_name, repo)
    r = requests.get(url)
    json = r.json()
    try:
        for commit in json:
            print("{}: {}".format(commit.get("sha"),
                                  commit.get("commit").
                                  get("author").get("name")))
    except Exception:
        print('None')
