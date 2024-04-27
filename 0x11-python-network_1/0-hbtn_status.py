#!/usr/bin/python3
'''script to fetch a url'''
import urllib
import urllib.parse
import urllib.request


if __name__ == '__main__':
    '''get request'''
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        print("Body response:")
        print(f"\t- type: {type(r.read())}")
        print(f"\t- content: {r.read()}")
        print(f"\t- utf8 content: {r.read().decode('utf-8')}")
