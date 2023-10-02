#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1 and len(sys.argv[1]) < 2:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ''}
    r = requests.post(url, data)
    try:
        json = r.json()
        if json:
            print('[{}] {}'.format(json['id'], json['name']))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
