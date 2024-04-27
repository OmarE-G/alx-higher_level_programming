#!/usr/bin/python3
import urllib
import urllib.parse
import urllib.request
'''script to fetch a url'''


if __name__ == '__main__':

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        print(f"\t- type: {type(r.read())}")
        print(f"\t- content: {r.read()}")
        print(f"\t- utf8 content: {r.read().decode('utf-8')}")
