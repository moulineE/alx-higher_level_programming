#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and
displays the body of the response with error code handeling
"""
import requests
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError:
        print('Error code: '.format(r.status_code))
