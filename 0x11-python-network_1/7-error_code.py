#!/usr/bin/python3
'''script to fetch a url'''
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with requests.get(url) as r:
        if r.status_code < 400:
            print(r.text)
        else:
            print(f"Error code: {r.status_code}")
