#!/usr/bin/python3
'''script to fetch a url'''
import urllib
import urllib.parse
import urllib.request


if __name__ == '__main__':
    '''get request'''
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        print("Body response:")
        content = r.read()
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
