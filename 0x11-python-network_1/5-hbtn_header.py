#!/usr/bin/python3
'''script to fetch a url'''
import requests
import sys


if __name__ == '__main__':
    '''get request'''
    url = sys.argv[1]
    r = requests.get(url)
    try:
        print(r.headers['X-Request-Id'])
    except KeyError:
        print(None)
