#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    passwd = sys.argv[2]
    r = requests.get(url, auth=(user, passwd))
    json = r.json()
    try:
        print(json['id'])
    except Exception:
        print('None')
