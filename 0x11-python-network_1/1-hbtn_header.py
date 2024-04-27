#!/usr/bin/python3
'''script to fetch a url'''
import urllib.request
import sys


if __name__ == '__main__':
    '''get request'''
    url = sys.argv[1]
    with urllib.request.urlopen(url) as r:
        print(r.headers['X-Request-Id'])
