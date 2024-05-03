#!/usr/bin/python3
'''get web page'''
import requests


if __name__ == '__main__':

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
