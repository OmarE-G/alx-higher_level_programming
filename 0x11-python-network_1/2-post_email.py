#!/usr/bin/python3
'''script to fetch a url'''
import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    '''post request'''
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')
    with urllib.request.urlopen(url, data) as r:
        print(r.read().decode('utf-8'))
