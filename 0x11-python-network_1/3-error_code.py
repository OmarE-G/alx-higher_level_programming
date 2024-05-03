#!/usr/bin/python3
'''script to fetch a url'''
import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    '''post request'''
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.status}")
